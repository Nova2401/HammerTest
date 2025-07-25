import random
import string

from django.db import models

def generate_invite_code():
    return ''.join(random.choices(string.ascii_uppercase + string.digits, k=6))


class User(models.Model):
    phone = models.CharField(max_length=15, unique=True, verbose_name="Номер")
    is_verified = models.BooleanField(default=False, verbose_name="Подтвержденный")
    invite_code = models.CharField(max_length=6, unique=True, default=generate_invite_code, verbose_name="Реферальный код")
    activated_invite = models.ForeignKey('self', null=True, blank=True, on_delete=models.SET_NULL, related_name='referrals', verbose_name="Реферал")
    created_at = models.DateTimeField(auto_now_add=True, verbose_name="Создан")


    def __str__(self):
        return self.phone

    class Meta:
        verbose_name = "Пользователь"
        verbose_name_plural = "Пользователи"