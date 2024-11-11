from django.contrib.auth.models import AbstractUser
from django.db import models

class CustomUser(AbstractUser):
    email = models.EmailField(unique=True)  # Уникальный email вместо username
    avatar = models.ImageField(upload_to='avatars/', blank=True, null=True)  # Аватар пользователя
    phone_number = models.CharField(max_length=15, blank=True, null=True)  # Телефон
    country = models.CharField(max_length=50, blank=True, null=True)  # Страна

    USERNAME_FIELD = 'email'  # Авторизация по email
    REQUIRED_FIELDS = ['username']  # Обязательное поле username
    class Meta:
        permissions = [
            ("view_all_mailings", "Can view all mailings"),
        ]