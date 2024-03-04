# Generated by Django 4.2 on 2024-02-23 10:01

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('users', '0005_doctor_date_joined_doctor_groups_doctor_is_active_and_more'),
    ]

    operations = [
        migrations.AddField(
            model_name='doctor',
            name='created',
            field=models.DateTimeField(auto_now_add=True, null=True, verbose_name='Дата создания'),
        ),
        migrations.AddField(
            model_name='doctor',
            name='updated',
            field=models.DateTimeField(auto_now=True, null=True, verbose_name='Дата обновления'),
        ),
        migrations.AddField(
            model_name='patientprofile',
            name='created',
            field=models.DateTimeField(auto_now_add=True, null=True, verbose_name='Дата создания'),
        ),
        migrations.AddField(
            model_name='patientprofile',
            name='updated',
            field=models.DateTimeField(auto_now=True, null=True, verbose_name='Дата обновления'),
        ),
        migrations.AddField(
            model_name='user',
            name='created',
            field=models.DateTimeField(auto_now_add=True, null=True, verbose_name='Дата создания'),
        ),
        migrations.AddField(
            model_name='user',
            name='updated',
            field=models.DateTimeField(auto_now=True, null=True, verbose_name='Дата обновления'),
        ),
    ]
