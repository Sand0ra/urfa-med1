from rest_framework.generics import ListAPIView

from apps.article import models
from apps.article.serializers import ArticleSerializer, BlogSerializer, QuestionnairesSerializer, NewsSerializer


# Create your views here.

class ArticleAPIViews(ListAPIView):
    queryset = models.Article.objects.all()
    serializer_class = ArticleSerializer
    lookup_field = 'article_slug'


class BlogAPIViews(ListAPIView):
    queryset = models.Blog.objects.all()
    serializer_class = BlogSerializer
    lookup_field = 'blog_slug'


class QuestionnairesAPIViews(ListAPIView):
    queryset = models.Questionnaires.objects.all()
    serializer_class = QuestionnairesSerializer
    lookup_field = 'qa_slug'


class NewsAPIViews(ListAPIView):
    queryset = models.News.objects.all()
    serializer_class = NewsSerializer
    lookup_field = 'news_slug'

