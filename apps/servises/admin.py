from django.contrib import admin
from .models import *


@admin.register(Region)
class RegionAdmin(admin.ModelAdmin):
    list_display = ('id', 'title')
    list_display_links = ('id', 'title')


@admin.register(Analysis)
class AnalysisAdmin(admin.ModelAdmin):
    fieldsets = [
        ('Русский перевод',
         {'fields': ['analyse_category', 'price', 'sale', 'promotion', 'analysis_name', 'Patient_instructions',
                     'procedure_description', 'expected_results', 'results_delivery_time']}),
        ('Кыргызский перевод', {'fields': ['analysis_name_ky', 'Patient_instructions_ky', 'procedure_description_ky',
                                           'expected_results_ky', 'results_delivery_time_ky']}),
        ('Английский перевод', {'fields': ['analysis_name_en', 'Patient_instructions_en', 'procedure_description_en',
                                           'expected_results_en', 'results_delivery_time_en']}),
        ('Турецкий перевод', {'fields': ['analysis_name_tr', 'Patient_instructions_tr', 'procedure_description_tr',
                                         'expected_results_tr', 'results_delivery_time_tr']}),
    ]
    list_display = ('id', 'analysis_name', 'analyse_category', 'price', 'sale', 'promotion')
    list_display_links = ('id', 'analysis_name')


@admin.register(AnalysisCategory)
class AnalysisСategoryAdmin(admin.ModelAdmin):
    fieldsets = [
        ('Русский перевод', {'fields': ['region', 'category_name', 'category_description']}),
        ('Кыргызский перевод', {'fields': ['category_name_ky', 'category_description_ky']}),
        ('Английский перевод', {'fields': ['category_name_en', 'category_description_en']}),
        ('Турецкий перевод', {'fields': ['category_name_tr', 'category_description_tr']}),
    ]
    list_display = ('id', 'region', 'category_name')
    list_display_links = ('id', 'category_name')


@admin.register(RehabilitationCategory)
class RehabilitationCategoryAdmin(admin.ModelAdmin):
    fieldsets = [
        ('Русский перевод', {'fields': ['region', 'rehabilitation_category_name', ]}),
        ('Кыргызский перевод', {'fields': ['rehabilitation_category_name_ky', ]}),
        ('Английский перевод', {'fields': ['rehabilitation_category_name_en', ]}),
        ('Турецкий перевод', {'fields': ['rehabilitation_category_name_tr', ]}),
    ]
    list_display = ('id', 'region', 'rehabilitation_category_name')
    list_display_links = ('id', 'rehabilitation_category_name')


@admin.register(Rehabilitation)
class RehabilitationAdmin(admin.ModelAdmin):
    fieldsets = [
        ('Русский перевод',
         {'fields': ['rehabilitation_category', 'rehabilitation_name', 'image', 'rehabilitation_description', ]}),
        ('Кыргызский перевод', {'fields': ['rehabilitation_name_ky', 'rehabilitation_description_ky', ]}),
        ('Английский перевод', {'fields': ['rehabilitation_name_en', 'rehabilitation_description_en', ]}),
        ('Турецкий перевод', {'fields': ['rehabilitation_name_tr', 'rehabilitation_description_tr', ]}),
    ]
    list_display = ('id', 'rehabilitation_name', 'rehabilitation_category', 'image')
    list_display_links = ('id', 'rehabilitation_name')


@admin.register(DiagnosticCategory)
class DiagnosticCategoryAdmin(admin.ModelAdmin):
    fieldsets = [
        ('Русский перевод', {'fields': ['region', 'diagnostic_category_name', ]}),
        ('Кыргызский перевод', {'fields': ['diagnostic_category_name_ky', ]}),
        ('Английский перевод', {'fields': ['diagnostic_category_name_en', ]}),
        ('Турецкий перевод', {'fields': ['diagnostic_category_name_tr', ]}),
    ]
    list_display = ('id', 'region', 'diagnostic_category_name')
    list_display_links = ('id', 'diagnostic_category_name')


@admin.register(DiagnosticSubcategory)
class DiagnosticSubcategoryAdmin(admin.ModelAdmin):
    fieldsets = [
        ('Русский перевод',
         {'fields': ['diagnostic_category', 'diagnostic_subcategory_name', 'diagnostic_subcategory_description', ]}),
        ('Кыргызский перевод',
         {'fields': ['diagnostic_subcategory_name_ky', 'diagnostic_subcategory_description_ky', ]}),
        ('Английский перевод',
         {'fields': ['diagnostic_subcategory_name_en', 'diagnostic_subcategory_description_en', ]}),
        ('Турецкий перевод', {'fields': ['diagnostic_subcategory_name_tr', 'diagnostic_subcategory_description_tr', ]}),
    ]
    list_display = ('id', 'diagnostic_category', 'diagnostic_subcategory_name')
    list_display_links = ('id', 'diagnostic_subcategory_name')


@admin.register(Diagnostic)
class DiagnosticAdmin(admin.ModelAdmin):
    fieldsets = [
        ('Русский перевод', {'fields': ['diagnostic_subcategory', 'diagnostic_name',
                                        'image', 'sale', 'promotion', 'description', ]}),
        ('Кыргызский перевод', {'fields': ['diagnostic_name_ky', 'description_ky', ]}),
        ('Английский перевод', {'fields': ['diagnostic_name_en', 'description_en', ]}),
        ('Турецкий перевод', {'fields': ['diagnostic_name_tr', 'description_tr', ]}),
    ]
    list_display = ('id', 'diagnostic_name', 'diagnostic_subcategory', 'image', 'sale', 'promotion')
    list_display_links = ('id', 'diagnostic_name')


@admin.register(PolyclinicCategory)
class PolyclinicCategoryAdmin(admin.ModelAdmin):
    fieldsets = [
        ('Русский перевод', {'fields': ['region', 'polyclinic_category_name', ]}),
        ('Кыргызский перевод', {'fields': ['polyclinic_category_name_ky', ]}),
        ('Английский перевод', {'fields': ['polyclinic_category_name_en', ]}),
        ('Турецкий перевод', {'fields': ['polyclinic_category_name_tr', ]}),
    ]
    list_display = ('id', 'region', 'polyclinic_category_name')
    list_display_links = ('id', 'polyclinic_category_name')


@admin.register(Polyclinic)
class PolyclinicAdmin(admin.ModelAdmin):
    fieldsets = [
        ('Русский перевод',
         {'fields': ['polyclinic_category', 'polyclinic_name', 'price_first_meet', 'price_second_meet',
                     'about_service', 'about_procedure', ]}),
        ('Кыргызский перевод', {'fields': ['polyclinic_name_ky', 'about_service_ky', 'about_procedure_ky']}),
        ('Английский перевод', {'fields': ['polyclinic_name_en', 'about_service_en', 'about_procedure_en']}),
        ('Турецкий перевод', {'fields': ['polyclinic_name_tr', 'about_service_tr', 'about_procedure_tr']}),
    ]
    list_display = ('id', 'polyclinic_name', 'polyclinic_category', 'price_first_meet', 'price_second_meet')
    list_display_links = ('id', 'polyclinic_name')


@admin.register(AddressCenter)
class AddressCenterAdmin(admin.ModelAdmin):
    fieldsets = [
        ('Русский перевод', {'fields': ['title', 'description', ]}),
        ('Кыргызский перевод', {'fields': ['title_ky', 'description_ky']}),
        ('Английский перевод', {'fields': ['title_en', 'description_en']}),
        ('Турецкий перевод', {'fields': ['title_tr', 'description_tr']}),
    ]
    list_display = ('id', 'title')
    list_display_links = ('id', 'title')
