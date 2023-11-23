from django.db import models
from django.contrib.auth.models import AbstractUser
from django.conf import settings
from django.core.mail import send_mail


class CustomUser(AbstractUser):
    email = models.EmailField(
        unique=True,
        verbose_name="Эл. почта",
        error_messages={
            "unique": "Аккаунт с данной электронной почтой уже существует.",
        },
    )
    registration_date = models.DateTimeField(auto_now_add=True, verbose_name="Дата регистрации")

    def __str__(self):
        return self.username
