# Generated by Django 4.2 on 2024-02-18 09:06

from django.conf import settings
from django.db import migrations, models
import django.db.models.deletion
import django.utils.timezone
import phonenumber_field.modelfields


class Migration(migrations.Migration):

    dependencies = [
        ('auth', '0012_alter_user_first_name_max_length'),
        ('servises', '0001_initial'),
        ('users', '0004_doctor_first_name_en_doctor_first_name_ru_and_more'),
    ]

    operations = [
        migrations.AddField(
            model_name='doctor',
            name='date_joined',
            field=models.DateTimeField(default=django.utils.timezone.now, verbose_name='date joined'),
        ),
        migrations.AddField(
            model_name='doctor',
            name='groups',
            field=models.ManyToManyField(blank=True, related_name='doctor_set', related_query_name='doctor', to='auth.group', verbose_name='Группы'),
        ),
        migrations.AddField(
            model_name='doctor',
            name='is_active',
            field=models.BooleanField(default=True, help_text='Designates whether this user should be treated as active. Unselect this instead of deleting accounts.', verbose_name='active'),
        ),
        migrations.AddField(
            model_name='doctor',
            name='is_staff',
            field=models.BooleanField(default=False, help_text='Designates whether the user can log into this admin site.', verbose_name='staff status'),
        ),
        migrations.AddField(
            model_name='doctor',
            name='is_superuser',
            field=models.BooleanField(default=False, help_text='Designates that this user has all permissions without explicitly assigning them.', verbose_name='superuser status'),
        ),
        migrations.AddField(
            model_name='doctor',
            name='last_login',
            field=models.DateTimeField(blank=True, null=True, verbose_name='last login'),
        ),
        migrations.AddField(
            model_name='doctor',
            name='password',
            field=models.CharField(default='', max_length=128, verbose_name='password'),
            preserve_default=False,
        ),
        migrations.AddField(
            model_name='doctor',
            name='phone_number',
            field=phonenumber_field.modelfields.PhoneNumberField(max_length=128, null=True, region=None, unique=True, verbose_name='номер телефона'),
        ),
        migrations.AddField(
            model_name='doctor',
            name='region',
            field=models.ForeignKey(null=True, on_delete=django.db.models.deletion.DO_NOTHING, to='servises.region', verbose_name='Регион'),
        ),
        migrations.AddField(
            model_name='doctor',
            name='user_permissions',
            field=models.ManyToManyField(blank=True, related_name='doctor_set', related_query_name='doctor', to='auth.permission', verbose_name='Права доступа'),
        ),
        migrations.AddField(
            model_name='patientprofile',
            name='phone_number',
            field=phonenumber_field.modelfields.PhoneNumberField(blank=True, max_length=128, null=True, region=None, unique=True, verbose_name='номер телефона'),
        ),
        migrations.AlterField(
            model_name='doctor',
            name='first_name',
            field=models.CharField(max_length=100, verbose_name='Имя'),
        ),
        migrations.AlterField(
            model_name='doctor',
            name='first_name_en',
            field=models.CharField(max_length=100, null=True, verbose_name='Имя'),
        ),
        migrations.AlterField(
            model_name='doctor',
            name='first_name_ru',
            field=models.CharField(max_length=100, null=True, verbose_name='Имя'),
        ),
        migrations.AlterField(
            model_name='doctor',
            name='first_name_tr',
            field=models.CharField(max_length=100, null=True, verbose_name='Имя'),
        ),
        migrations.AlterField(
            model_name='doctor',
            name='last_name',
            field=models.CharField(max_length=100, verbose_name='Фамилия'),
        ),
        migrations.AlterField(
            model_name='doctor',
            name='last_name_en',
            field=models.CharField(max_length=100, null=True, verbose_name='Фамилия'),
        ),
        migrations.AlterField(
            model_name='doctor',
            name='last_name_ru',
            field=models.CharField(max_length=100, null=True, verbose_name='Фамилия'),
        ),
        migrations.AlterField(
            model_name='doctor',
            name='last_name_tr',
            field=models.CharField(max_length=100, null=True, verbose_name='Фамилия'),
        ),
        migrations.AlterField(
            model_name='doctor',
            name='specialization',
            field=models.TextField(default='Доктор практикант', null=True, verbose_name='Специализация'),
        ),
        migrations.AlterField(
            model_name='doctor',
            name='specialization_en',
            field=models.TextField(default='Доктор практикант', null=True, verbose_name='Специализация'),
        ),
        migrations.AlterField(
            model_name='doctor',
            name='specialization_ru',
            field=models.TextField(default='Доктор практикант', null=True, verbose_name='Специализация'),
        ),
        migrations.AlterField(
            model_name='doctor',
            name='specialization_tr',
            field=models.TextField(default='Доктор практикант', null=True, verbose_name='Специализация'),
        ),
        migrations.AlterField(
            model_name='patientprofile',
            name='birth_date',
            field=models.DateField(blank=True, null=True, verbose_name='Дата рождения'),
        ),
        migrations.AlterField(
            model_name='patientprofile',
            name='user',
            field=models.OneToOneField(on_delete=django.db.models.deletion.CASCADE, related_name='patient_profile', to=settings.AUTH_USER_MODEL, verbose_name='Пациент'),
        ),
        migrations.AlterField(
            model_name='user',
            name='birth_date',
            field=models.DateField(null=True, verbose_name='Дата рождения'),
        ),
        migrations.AlterField(
            model_name='user',
            name='gender',
            field=models.CharField(choices=[('Man', 'Мужской'), ('Women', 'Женский')], max_length=10, null=True, verbose_name='Пол'),
        ),
        migrations.AlterField(
            model_name='user',
            name='phone_number',
            field=phonenumber_field.modelfields.PhoneNumberField(max_length=128, null=True, region=None, unique=True, verbose_name='номер телефона'),
        ),
    ]
