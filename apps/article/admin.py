from django.contrib import admin
from .models import *


@admin.register(Article)
class ArticleAdmin(admin.ModelAdmin):
    fieldsets = [
        ('Русский перевод', {'fields': ['title', 'image', 'description']}),
        ('Кыргызский перевод', {'fields': ['title_ky', 'description_ky']}),
        ('Английский перевод', {'fields': ['title_en', 'description_en']}),
        ('Турецкий перевод', {'fields': ['title_tr', 'description_tr']}),
    ]
    list_display = ('id', 'title', 'pub_date')
    list_display_links = ('id', 'title',)


@admin.register(Blog)
class BlogAdmin(admin.ModelAdmin):
    fieldsets = [
        ('Русский перевод', {'fields': ['title', 'description']}),
        ('Кыргызский перевод', {'fields': ['title_ky', 'description_ky']}),
        ('Английский перевод', {'fields': ['title_en', 'description_en']}),
        ('Турецкий перевод', {'fields': ['title_tr', 'description_tr']}),
    ]
    list_display = ('id', 'title', 'pub_date')
    list_display_links = ('id', 'title',)


@admin.register(Questionnaires)
class QuestionnairesAdmin(admin.ModelAdmin):
    fieldsets = [
        ('Русский перевод', {'fields': ['title', 'question', 'answer']}),
        ('Кыргызский перевод', {'fields': ['title_ky', 'question_ky', 'answer_ky']}),
        ('Английский перевод', {'fields': ['title_en', 'question_en', 'answer_en']}),
        ('Турецкий перевод', {'fields': ['title_tr', 'question_tr', 'answer_tr']}),
    ]
    list_display = ('id', 'title', 'question', 'answer', 'pub_date')
    list_display_links = ('id', 'title',)


@admin.register(News)
class NewsAdmin(admin.ModelAdmin):
    fieldsets = [
        ('Русский перевод', {'fields': ['title', 'description']}),
        ('Кыргызский перевод', {'fields': ['title_ky', 'description_ky']}),
        ('Английский перевод', {'fields': ['title_en', 'description_en']}),
        ('Турецкий перевод', {'fields': ['title_tr', 'description_tr']}),
    ]
    list_display = ('id', 'title', 'pub_date')
    list_display_links = ('id', 'title',)
