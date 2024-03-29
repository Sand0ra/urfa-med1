# Generated by Django 4.2 on 2024-02-23 10:29

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('servises', '0003_addresscenter_created_addresscenter_updated_and_more'),
    ]

    operations = [
        migrations.CreateModel(
            name='AnalysisCategory',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('category_name', models.CharField(max_length=255, verbose_name='Категорий анализа')),
                ('category_name_ru', models.CharField(max_length=255, null=True, verbose_name='Категорий анализа')),
                ('category_name_en', models.CharField(max_length=255, null=True, verbose_name='Категорий анализа')),
                ('category_name_tr', models.CharField(max_length=255, null=True, verbose_name='Категорий анализа')),
                ('category_description', models.TextField(verbose_name='Описание Категория')),
                ('category_description_ru', models.TextField(null=True, verbose_name='Описание Категория')),
                ('category_description_en', models.TextField(null=True, verbose_name='Описание Категория')),
                ('category_description_tr', models.TextField(null=True, verbose_name='Описание Категория')),
                ('created', models.DateTimeField(auto_now_add=True, null=True, verbose_name='Дата создания')),
                ('updated', models.DateTimeField(auto_now=True, null=True, verbose_name='Дата обновления')),
                ('region', models.ForeignKey(on_delete=django.db.models.deletion.DO_NOTHING, to='servises.region', verbose_name='Регион')),
            ],
            options={
                'verbose_name': 'Категорий анализа',
                'verbose_name_plural': 'Категории анализов',
            },
        ),
        migrations.RemoveField(
            model_name='analysis',
            name='region',
        ),
        migrations.DeleteModel(
            name='AnalysisSubcategory',
        ),
        migrations.AddField(
            model_name='analysis',
            name='analyse_category',
            field=models.ForeignKey(null=True, on_delete=django.db.models.deletion.DO_NOTHING, to='servises.analysiscategory', verbose_name='Категорий анализа'),
        ),
    ]
