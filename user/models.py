from django.contrib.auth.models import AbstractUser
from django.db import models

MAX_LENGHT = 150


class CustomUser(AbstractUser):
    """Custom user model for testing."""
    email = models.EmailField(
        'Адрес электронной почты',
        max_length=254,
        blank=False,
        null=False,
        unique=True)
    username = models.CharField(
        'Логин',
        max_length=MAX_LENGHT,
        blank=False,
        null=False)
    first_name = models.CharField(
        'Имя',
        max_length=MAX_LENGHT,
        blank=False,
        null=False)
    last_name = models.CharField(
        'Фамилия',
        max_length=MAX_LENGHT,
        blank=False,
        null=False)
    password = models.CharField(
        'Пароль',
        max_length=MAX_LENGHT,
        blank=False,
        null=False)

    USERNAME_FIELD = 'email'
    REQUIRED_FIELDS = ['username']

    class Meta:
        verbose_name = 'пользователь'
        verbose_name_plural = 'Пользователи'
        unique_together = ('email', 'username')
