from rest_framework import serializers

from apps.article.models import *


class ArticleSerializer(serializers.ModelSerializer):
    class Meta:
        model = Article
        fields = ('title', 'article_slug', 'pub_date', 'description', 'image')
        read_only_fields = ['article_slug']


class BlogSerializer(serializers.ModelSerializer):
    class Meta:
        model = Blog
        fields = ('title', 'blog_slug', 'pub_date', 'description')


class QuestionnairesSerializer(serializers.ModelSerializer):
    class Meta:
        model = Questionnaires
        fields = ('title', 'qa_slug', 'question', 'pub_date')


class NewsSerializer(serializers.ModelSerializer):
    class Meta:
        model = News
        fields = ('title', 'news_slug', 'pub_date', 'description')
