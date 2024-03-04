from django.db import models
from django.contrib.auth.models import Group, Permission
from django.contrib.auth.base_user import BaseUserManager
from django.contrib.auth.models import AbstractUser
from django.utils.crypto import get_random_string
from phonenumber_field.modelfields import PhoneNumberField
from django.dispatch import receiver
from django.db.models.signals import post_save

from apps.servises.models import Region
from config import settings


class CustomUserManager(BaseUserManager):
    def create_user(self, phone_number, password=None, **extra_fields):
        if not phone_number:
            raise ValueError('Не указан номер телефона')
        user = self.model(phone_number=phone_number, **extra_fields)
        user.set_password(password)
        user.save()
        return user

    def create_superuser(self, phone_number, password, **extra_fields):
        extra_fields.setdefault('is_staff', True)
        extra_fields.setdefault('is_superuser', True)
        extra_fields.setdefault('is_active', True)
        return self.create_user(phone_number, password, **extra_fields)


class User(AbstractUser):
    email = None
    username = None
    phone_number = PhoneNumberField('номер телефона', unique=True, null=True, blank=False)
    middle_name = models.CharField('Отчество', max_length=100, null=True, blank=True)
    birth_date = models.DateField('Дата рождения', null=True, blank=False)
    gender = models.CharField('Пол', max_length=10, choices=[
        ('Man', 'Мужской'),
        ('Women', 'Женский'),
    ], null=True, blank=False)
    upcoming_appointment = models.DateTimeField(null=True, blank=True)
    history = models.TextField(null=True, blank=True)
    created = models.DateTimeField(auto_now_add=True, verbose_name="Дата создания", null=True)
    updated = models.DateTimeField(auto_now=True, verbose_name="Дата обновления", null=True)

    USERNAME_FIELD = 'phone_number'
    REQUIRED_FIELDS = []

    objects = CustomUserManager()

    class Meta:
        verbose_name = 'Пациент'
        verbose_name_plural = 'Пациенты'

    def __str__(self):
        return str(self.phone_number) if self.phone_number else "Номер телефона не указан"


class PasswordResetCode(models.Model):
    user = models.ForeignKey(settings.AUTH_USER_MODEL, on_delete=models.CASCADE)
    code = models.CharField(max_length=6)
    created_at = models.DateTimeField(auto_now_add=True)

    def save(self, *args, **kwargs):
        if not self.code:
            self.code = self.generate_code()
        return super().save(*args, **kwargs)

    def generate_code(self):
        return get_random_string(length=6, allowed_chars='0123456789')

    def send_reset_code(self):
        subject = 'Код сброса пароля'
        message = f'Ваш код сброса пароля: {self.code}'
        print(self.code)
        return message
