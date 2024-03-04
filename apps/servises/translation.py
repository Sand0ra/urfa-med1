from modeltranslation.translator import register, TranslationOptions
from .models import *


@register(Region)
class RegionTranslationOptions(TranslationOptions):
    fields = ('title',)


@register(Analysis)
class AnalysisTranslationOptions(TranslationOptions):
    fields = ('analysis_name', 'analysis_description', 'Patient_instructions', 'procedure_description',
              'expected_results', 'results_delivery_time')


@register(AnalysisCategory)
class AnalysisSubcategoryTranslationOptions(TranslationOptions):
    fields = ('category_name', 'category_description')


@register(RehabilitationCategory)
class RehabilitationCategoryTranslationOptions(TranslationOptions):
    fields = ('rehabilitation_category_name',)


@register(Rehabilitation)
class RehabilitationTranslationOptions(TranslationOptions):
    fields = ('rehabilitation_name', 'rehabilitation_description',)


@register(DiagnosticCategory)
class DiagnosticCategoryTranslationOptions(TranslationOptions):
    fields = ('diagnostic_category_name',)


@register(DiagnosticSubcategory)
class DiagnosticSubcategoryTranslationOptions(TranslationOptions):
    fields = ('diagnostic_subcategory_name', 'diagnostic_subcategory_description')


@register(Diagnostic)
class DiagnosticTranslationOptions(TranslationOptions):
    fields = ('diagnostic_name', 'description',)


@register(PolyclinicCategory)
class PolyclinicCategoryTranslationOptions(TranslationOptions):
    fields = ('polyclinic_category_name',)


@register(Polyclinic)
class PolyclinicTranslationOptions(TranslationOptions):
    fields = ('polyclinic_name', 'about_service', 'about_procedure')


@register(AddressCenter)
class AddressCenterTranslationOptions(TranslationOptions):
    fields = ('title', 'description')
