from modeltranslation.translator import register, TranslationOptions
from .models import *


@register(AboutCompany)
class AboutCompanyTranslationOptions(TranslationOptions):
    fields = ('title', 'description')


@register(OurExperience)
class OurExperienceTranslationOptions(TranslationOptions):
    fields = ('title', 'description')


@register(OurCommand)
class OurCommandTranslationOptions(TranslationOptions):
    fields = ('title', 'description')


@register(OurCommandProfession)
class OurCommandSpecialhostTranslationOptions(TranslationOptions):
    fields = ('title', 'description',)


@register(Vacancy)
class VacancyTranslationOptions(TranslationOptions):
    fields = ('title', 'requirements', 'responsibilities', 'conditions')
