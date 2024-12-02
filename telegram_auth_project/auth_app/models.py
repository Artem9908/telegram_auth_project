from django.db import models
from django.contrib.auth.models import User

class TelegramToken(models.Model):
    user = models.ForeignKey(User, on_delete=models.CASCADE)
    token = models.CharField(max_length=64, unique=True)
    is_used = models.BooleanField(default=False)
    is_authenticated = models.BooleanField(default=False)  # Добавлено поле
