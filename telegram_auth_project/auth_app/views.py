import uuid
from django.shortcuts import render, redirect
from django.contrib.auth.models import User
from .models import TelegramToken
from django.contrib.auth import login
from django.http import HttpResponse
import requests
import json
from django.http import JsonResponse
from django.views.decorators.csrf import csrf_exempt

def home(request):
    if request.user.is_authenticated:
        return render(request, 'auth_app/home.html', {'username': request.user.username})
    else:
        return render(request, 'auth_app/home.html')

def generate_token(request):
    if not request.user.is_authenticated:
        # Создание временного пользователя
        user = User.objects.create(username=str(uuid.uuid4()))
        user.set_unusable_password()
        user.save()
    else:
        user = request.user

    # Генерация уникального токена
    token = str(uuid.uuid4())
    TelegramToken.objects.create(user=user, token=token)

    # Сохраняем токен в сессии
    request.session['auth_token'] = token

    # Ссылка на Telegram-бота с токеном
    bot_username = 'myauthtest_bot'  # Замените на имя вашего бота
    telegram_link = f'https://t.me/{bot_username}?start={token}'

    return redirect(telegram_link)


@csrf_exempt
def telegram_callback(request):
    if request.method == 'POST':
        data = json.loads(request.body.decode('utf-8'))
        message = data.get('message', {})
        text = message.get('text', '')
        chat = message.get('chat', {})
        username = chat.get('username', '')

        if text.startswith('/start '):
            token = text.split('/start ')[1]
            try:
                tg_token = TelegramToken.objects.get(token=token, is_used=False)
                tg_token.is_used = True
                tg_token.is_authenticated = True  # Обновляем статус авторизации
                tg_token.save()

                # Обновление информации о пользователе
                user = tg_token.user
                user.username = username
                user.save()

                return HttpResponse('Авторизация успешна')
            except TelegramToken.DoesNotExist:
                return HttpResponse('Неверный токен')
    return HttpResponse('OK')


def check_auth(request):
    is_authenticated = False
    if request.user.is_authenticated:
        is_authenticated = True
    else:
        token = request.session.get('auth_token')
        if token:
            try:
                tg_token = TelegramToken.objects.get(token=token, is_authenticated=True)
                # Авторизуем пользователя
                login(request, tg_token.user)
                is_authenticated = True
            except TelegramToken.DoesNotExist:
                pass
    return JsonResponse({'is_authenticated': is_authenticated})