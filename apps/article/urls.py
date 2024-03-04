from django.urls import path

from apps.article.views import *

urlpatterns = [
    path(r'articles/', ArticleAPIViews.as_view(), name='api_article'),
    path('blogs/', BlogAPIViews.as_view(), name='api_blog'),
    path('questionnaires/', QuestionnairesAPIViews.as_view(), name='api_questionnaires'),
    path('news/', NewsAPIViews.as_view(), name='api_news')
]


