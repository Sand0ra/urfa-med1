from modeltranslation.translator import register, TranslationOptions
from .models import *


@register(Article)
class ArticleTranslationOptions(TranslationOptions):
    fields = ('title', 'description',)


@register(Blog)
class BlogTranslationOptions(TranslationOptions):
    fields = ('title', 'description',)


@register(Questionnaires)
class QuestionnairesTranslationOptions(TranslationOptions):
    fields = ('title', 'question', 'answer')


@register(News)
class NewsTranslationOptions(TranslationOptions):
    fields = ('title', 'description',)

