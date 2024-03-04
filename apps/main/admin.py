from django.contrib import admin

from apps.main.models import *


@admin.register(AboutCompany)
class AboutCompanyAdmin(admin.ModelAdmin):
    fieldsets = [
        ('Русский перевод', {'fields': ['title', 'image', 'description']}),
        ('Кыргызский перевод', {'fields': ['title_ky', 'description_ky']}),
        ('Английский перевод', {'fields': ['title_en', 'description_en']}),
        ('Турецкий перевод', {'fields': ['title_tr', 'description_tr']}),
    ]
    list_display = ('id', 'title', 'image')
    list_display_links = ('id', 'title',)


@admin.register(OurExperience)
class OurExperienceAdmin(admin.ModelAdmin):
    fieldsets = [
        ('Русский перевод', {'fields': ['title', 'image', 'description']}),
        ('Кыргызский перевод', {'fields': ['title_ky', 'description_ky']}),
        ('Английский перевод', {'fields': ['title_en', 'description_en']}),
        ('Турецкий перевод', {'fields': ['title_tr', 'description_tr']}),
    ]
    list_display = ('id', 'title',  'image')
    list_display_links = ('id', 'title',)


@admin.register(OurCommandProfession)
class OurCommandSpecialhostAdmin(admin.ModelAdmin):
    fieldsets = [
        ('Русский перевод', {'fields': ['title', 'description']}),
        ('Кыргызский перевод', {'fields': ['title_ky', 'description_ky']}),
        ('Английский перевод', {'fields': ['title_en', 'description_en']}),
        ('Турецкий перевод', {'fields': ['title_tr', 'description_tr']}),
    ]
    list_display = ('id', 'title')
    list_display_links = ('id', 'title',)


@admin.register(OurCommand)
class OurCommandAdmin(admin.ModelAdmin):
    fieldsets = [
        ('Русский перевод', {'fields': ['profession', 'title', 'description']}),
        ('Кыргызский перевод', {'fields': ['title_ky', 'description_ky']}),
        ('Английский перевод', {'fields': ['title_en', 'description_en']}),
        ('Турецкий перевод', {'fields': ['title_tr', 'description_tr']}),
    ]
    list_display = ('id', 'title', 'profession')
    list_display_links = ('id', 'title',)


@admin.register(Vacancy)
class VacancyAdmin(admin.ModelAdmin):
    fieldsets = [
        ('Русский перевод', {'fields': ['title', 'requirements', 'responsibilities', 'conditions']}),
        ('Кыргызский перевод', {'fields': ['title_ky', 'requirements_ky', 'responsibilities_ky', 'conditions_ky']}),
        ('Английский перевод', {'fields': ['title_en', 'requirements_en', 'responsibilities_en', 'conditions_en']}),
        ('Турецкий перевод', {'fields': ['title_tr', 'requirements_tr', 'responsibilities_tr', 'conditions_tr']}),
    ]
    list_display = ('id', 'title', 'pub_date', 'requirements')
    list_display_links = ('id', 'title',)
