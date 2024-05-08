from django.db import models

from django.contrib.auth.models import AbstractUser


class User(AbstractUser):
    username = None

    email = models.EmailField(
        unique=True,
        verbose_name='email'
    )
    is_active = models.BooleanField(
        default=True,
        verbose_name='is_active'
    )
    chat_id = models.CharField(
        max_length=255,
        verbose_name='number_of_chat',
        blank=True,
        null=True
    )

    USERNAME_FIELD = 'email'
    REQUIRED_FIELDS = []

    def __str__(self):
        return f'{self.email} {self.is_active}'

    class Meta:
        verbose_name = 'пользователь'
        verbose_name_plural = 'пользователи'
