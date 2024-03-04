from django.contrib.auth.forms import UserCreationForm
from django import forms

from apps.users.models import User


class PatientRegisterForm(UserCreationForm):
    first_name = forms.CharField(label='Имя', required=True)
    last_name = forms.CharField(label='Фамилия', required=True)

    class Meta(UserCreationForm.Meta):
        model = User
        fields = ['phone_number', 'first_name', 'last_name', 'middle_name', 'birth_date',
                  'gender', 'upcoming_appointment', 'history', ]
