# Generated by Django 4.2 on 2024-02-23 10:29

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('article', '0005_article_created_article_updated_blog_created_and_more'),
    ]

    operations = [
        migrations.AlterField(
            model_name='article',
            name='image',
            field=models.ImageField(blank=True, null=True, upload_to='article_images/', verbose_name='Изображение'),
        ),
    ]
