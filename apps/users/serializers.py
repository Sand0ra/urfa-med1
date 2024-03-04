from rest_framework import serializers
from rest_framework.exceptions import ValidationError

from .models import User
from .validators import _validate_password, _validate_phone_number


class UserListSerializer(serializers.ModelSerializer):

    class Meta:
        model = User
        fields = ['phone_number', 'first_name', 'last_name', 'middle_name', 'birth_date',
                  'gender', 'upcoming_appointment', 'history', 'password']

    def create(self, validated_data):
        user = User.objects.create_user(**validated_data)
        return user


class PatientProfileSerializer(serializers.ModelSerializer):
    password = serializers.CharField(write_only=True, required=True, validators=[_validate_password])

    class Meta:
        model = User
        fields = ['phone_number', 'first_name', 'last_name', 'middle_name', 'birth_date',
                  'gender', 'upcoming_appointment', 'history', 'password']
        read_only_fields = ['phone_number', 'upcoming_appointment', 'history']
        required_fields = ['first_name', 'last_name', 'middle_name', 'birth_date', 'gender']
        error_messages = {
            'required': 'Обязательное поле.',
            'blank': 'Поле не может быть пустым.',
            'invalid': 'Неверный формат.',
        }
        default_error_messages = {
            'invalid_data': 'Неверные данные.',
            'invalid_model': 'Неверный модель.',
        }

    def save(self, **kwargs):
        user = self.instance
        user.set_password(self.validated_data['password'])
        user.save()
        return user


class CustomPasswordResetSerializer(serializers.Serializer):
    phone_number = serializers.CharField(validators=[_validate_phone_number])

    def validate_phone_number(self, value):
        user = User.objects.filter(phone_number=value).first()
        if not user:
            raise ValidationError("Пользователь с таким номером телефона не существует.")
        return value

    def save(self):
        phone_number = self.validated_data.get("phone_number")
        user = User.objects.get(phone_number=phone_number)
        return phone_number, user


class ResetPasswordSerializer(serializers.Serializer):
    phone_number = serializers.CharField()
    reset_code = serializers.CharField()
    new_password = serializers.CharField(validators=[_validate_password])
    confirm_password = serializers.CharField()

    def validate(self, attrs):
        new_password = attrs.get('new_password')
        confirm_password = attrs.get('confirm_password')

        if new_password != confirm_password:
            raise ValidationError("Пароли не совпадают")
        return attrs
