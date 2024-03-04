import re
from django.core.exceptions import ValidationError

from rest_framework import serializers


def _validate_phone_number(value):
    pattern = r'^\+996\d{9}$'
    if not re.match(pattern, value):
        raise ValidationError('Номер телефона должен быть в действующем международном формате.')


def _validate_password(password):
    if len(password) < 8:
        raise serializers.ValidationError("Минимальная длина пароля - 8 символов")

    # Проверка наличия хотя бы одной буквы в верхнем регистре
    if not re.search(r'[A-Z]', password):
        raise serializers.ValidationError("Пароль должен содержать хотя бы одну заглавную букву")

    # Проверка наличия хотя бы одной буквы в нижнем регистре
    if not re.search(r'[a-z]', password):
        raise serializers.ValidationError("Пароль должен содержать хотя бы одну строчную букву")

    # Проверка наличия хотя бы одной цифры
    if not re.search(r'\d', password):
        raise serializers.ValidationError("Пароль должен содержать хотя бы одну цифру")

    return password
