from django.contrib import admin
from .models import *
from .forms import PatientRegisterForm
from django.contrib.auth import get_user_model

User = get_user_model()


@admin.register(User)
class UserAdmin(admin.ModelAdmin):
    form = PatientRegisterForm
    list_display = ('id', 'phone_number', 'first_name', 'last_name')
    list_display_links = ('id', 'phone_number')


admin.site.unregister(Group)
