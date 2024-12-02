from django.urls import path
from . import views

urlpatterns = [
    path('', views.home, name='home'),
    path('generate_token/', views.generate_token, name='generate_token'),
    path('telegram_callback/', views.telegram_callback, name='telegram_callback'),
    path('check_auth/', views.check_auth, name='check_auth'),  # Добавлено
]
