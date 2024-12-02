# Авторизация через Telegram-бота в Django

Это простое Django-приложение реализует авторизацию пользователей через Telegram-бота.

## Функциональность

- **Авторизация через Telegram**: Пользователь может войти на сайт, взаимодействуя с Telegram-ботом.
- **Отображение имени пользователя**: После авторизации на сайте отображается имя пользователя из Telegram.

## Установка и запуск

1. **Клонирование репозитория**

   ```bash
   git clone https://github.com/yourusername/telegram_auth_project.git
   cd telegram_auth_project
   ```

2. **Установка зависимостей**

   Установите необходимые пакеты:

   ```bash
   pip install django
   ```

3. **Применение миграций**

   ```bash
   python manage.py makemigrations
   python manage.py migrate
   ```

4. **Запуск сервера**

   ```bash
   python manage.py runserver
   ```

5. **Настройка Telegram-бота**

   - Создайте бота через [@BotFather](https://t.me/BotFather) и получите токен.
   - Установите Webhook для бота, используя `ngrok` для туннелирования вашего локального сервера в интернет.

6. **Запуск ngrok**

   ```bash
   ngrok http 8000
   ```

   Используйте полученный HTTPS URL для установки Webhook.

7. **Установка Webhook**

   ```bash
   curl "https://api.telegram.org/bot<ВашТокен>/setWebhook?url=<ВашHTTPSURL>/telegram_callback/"
   ```

## Использование

1. Перейдите на `http://127.0.0.1:8000/`.
2. Нажмите **"Войти через Telegram"**.
3. Вас перенаправит в Telegram-бота. Нажмите **"Start"**.
4. Вернитесь на сайт и обновите страницу. Ваше имя пользователя должно отобразиться.

## Автор

[Ваше имя](https://github.com/yourusername)
