# Generated by Django 4.2 on 2024-02-16 12:16

import ckeditor.fields
from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='AboutCompany',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('title', models.CharField(max_length=255, verbose_name='Название')),
                ('title_ru', models.CharField(max_length=255, null=True, verbose_name='Название')),
                ('title_en', models.CharField(max_length=255, null=True, verbose_name='Название')),
                ('title_tr', models.CharField(max_length=255, null=True, verbose_name='Название')),
                ('image', models.ImageField(upload_to='about_company_image/', verbose_name='Фотография')),
                ('description', ckeditor.fields.RichTextField(verbose_name='Описание')),
                ('description_ru', ckeditor.fields.RichTextField(null=True, verbose_name='Описание')),
                ('description_en', ckeditor.fields.RichTextField(null=True, verbose_name='Описание')),
                ('description_tr', ckeditor.fields.RichTextField(null=True, verbose_name='Описание')),
            ],
            options={
                'verbose_name': 'О Компании',
                'verbose_name_plural': 'О Компании',
            },
        ),
        migrations.CreateModel(
            name='OurCommandProfession',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('title', models.CharField(max_length=255, verbose_name='Название')),
                ('title_ru', models.CharField(max_length=255, null=True, verbose_name='Название')),
                ('title_en', models.CharField(max_length=255, null=True, verbose_name='Название')),
                ('title_tr', models.CharField(max_length=255, null=True, verbose_name='Название')),
                ('description', models.TextField(verbose_name='Описание')),
                ('description_ru', models.TextField(null=True, verbose_name='Описание')),
                ('description_en', models.TextField(null=True, verbose_name='Описание')),
                ('description_tr', models.TextField(null=True, verbose_name='Описание')),
            ],
            options={
                'verbose_name': 'Специальность нашей команды',
                'verbose_name_plural': 'Специальности нашей команды',
            },
        ),
        migrations.CreateModel(
            name='OurExperience',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('title', models.CharField(max_length=255, verbose_name='Название')),
                ('title_ru', models.CharField(max_length=255, null=True, verbose_name='Название')),
                ('title_en', models.CharField(max_length=255, null=True, verbose_name='Название')),
                ('title_tr', models.CharField(max_length=255, null=True, verbose_name='Название')),
                ('image', models.ImageField(upload_to='our_experience_image/', verbose_name='Фотография')),
                ('description', ckeditor.fields.RichTextField(verbose_name='Описание')),
                ('description_ru', ckeditor.fields.RichTextField(null=True, verbose_name='Описание')),
                ('description_en', ckeditor.fields.RichTextField(null=True, verbose_name='Описание')),
                ('description_tr', ckeditor.fields.RichTextField(null=True, verbose_name='Описание')),
            ],
            options={
                'verbose_name': 'Наш опыт',
                'verbose_name_plural': 'Наши опыты',
            },
        ),
        migrations.CreateModel(
            name='Vacancy',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('title', models.CharField(max_length=255, verbose_name='Название')),
                ('title_ru', models.CharField(max_length=255, null=True, verbose_name='Название')),
                ('title_en', models.CharField(max_length=255, null=True, verbose_name='Название')),
                ('title_tr', models.CharField(max_length=255, null=True, verbose_name='Название')),
                ('requirements', ckeditor.fields.RichTextField(verbose_name='Требования')),
                ('requirements_ru', ckeditor.fields.RichTextField(null=True, verbose_name='Требования')),
                ('requirements_en', ckeditor.fields.RichTextField(null=True, verbose_name='Требования')),
                ('requirements_tr', ckeditor.fields.RichTextField(null=True, verbose_name='Требования')),
                ('responsibilities', ckeditor.fields.RichTextField(verbose_name='Обязанности')),
                ('responsibilities_ru', ckeditor.fields.RichTextField(null=True, verbose_name='Обязанности')),
                ('responsibilities_en', ckeditor.fields.RichTextField(null=True, verbose_name='Обязанности')),
                ('responsibilities_tr', ckeditor.fields.RichTextField(null=True, verbose_name='Обязанности')),
                ('conditions', ckeditor.fields.RichTextField(verbose_name='Условия')),
                ('conditions_ru', ckeditor.fields.RichTextField(null=True, verbose_name='Условия')),
                ('conditions_en', ckeditor.fields.RichTextField(null=True, verbose_name='Условия')),
                ('conditions_tr', ckeditor.fields.RichTextField(null=True, verbose_name='Условия')),
            ],
            options={
                'verbose_name': 'Вакансия',
                'verbose_name_plural': 'Вакансии',
            },
        ),
        migrations.CreateModel(
            name='OurCommand',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('title', models.CharField(max_length=255, verbose_name='Название')),
                ('title_ru', models.CharField(max_length=255, null=True, verbose_name='Название')),
                ('title_en', models.CharField(max_length=255, null=True, verbose_name='Название')),
                ('title_tr', models.CharField(max_length=255, null=True, verbose_name='Название')),
                ('description', models.TextField(verbose_name='Описание')),
                ('description_ru', models.TextField(null=True, verbose_name='Описание')),
                ('description_en', models.TextField(null=True, verbose_name='Описание')),
                ('description_tr', models.TextField(null=True, verbose_name='Описание')),
                ('profession', models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.DO_NOTHING, to='main.ourcommandprofession', verbose_name='Специальность')),
            ],
            options={
                'verbose_name': 'Наша Команда',
                'verbose_name_plural': 'Наша Команда',
            },
        ),
    ]
