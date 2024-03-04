from django.db import models
from ckeditor.fields import RichTextField
from unidecode import unidecode
from django.utils.text import slugify


class Article(models.Model):
    title = models.CharField(verbose_name='Название', max_length=200)
    article_slug = models.SlugField(unique=True, blank=True, verbose_name='URL')
    pub_date = models.DateTimeField('Дата публикации', auto_now_add=True)
    description = RichTextField(verbose_name='Описание', null=True, blank=True)
    image = models.ImageField('Изображение', upload_to='article_images/', null=True, blank=True)
    created = models.DateTimeField(auto_now_add=True, verbose_name="Дата создания", null=True)
    updated = models.DateTimeField(auto_now=True, verbose_name="Дата обновления", null=True)

    def save(self, *args, **kwargs):
        self.article_slug = slugify(unidecode(self.title))
        super().save(*args, **kwargs)

    def __str__(self):
        return self.title

    class Meta:
        verbose_name = 'Статья'
        verbose_name_plural = 'Статьи'


class Blog(models.Model):
    title = models.CharField(verbose_name='Название блога', max_length=200)
    blog_slug = models.SlugField(unique=True, blank=True, verbose_name='URL')
    pub_date = models.DateTimeField('Дата публикации', auto_now_add=True)
    description = RichTextField(verbose_name='Описание', null=True, blank=True)
    created = models.DateTimeField(auto_now_add=True, verbose_name="Дата создания", null=True)
    updated = models.DateTimeField(auto_now=True, verbose_name="Дата обновления", null=True)

    def save(self, *args, **kwargs):
        self.blog_slug = slugify(unidecode(self.title))
        super().save(*args, **kwargs)

    def __str__(self):
        return self.title

    class Meta:
        verbose_name = 'Блог'
        verbose_name_plural = 'Блог'


class Questionnaires(models.Model):
    title = models.CharField(verbose_name='Название FAQ', max_length=200)
    qa_slug = models.SlugField(unique=True, blank=True)
    pub_date = models.DateTimeField('Дата публикации', auto_now_add=True)
    question = RichTextField(verbose_name='Вопросы')
    answer = RichTextField(verbose_name='Ответы')
    created = models.DateTimeField(auto_now_add=True, verbose_name="Дата создания", null=True)
    updated = models.DateTimeField(auto_now=True, verbose_name="Дата обновления", null=True)

    def save(self, *args, **kwargs):
        self.qa_slug = slugify(unidecode(self.title))
        super().save(*args, **kwargs)

    def __str__(self):
        return self.title

    class Meta:
        verbose_name = 'Частый вопрос'
        verbose_name_plural = 'Частые вопросы'


class News(models.Model):
    title = models.CharField(verbose_name='Новость', max_length=200)
    news_slug = models.SlugField(unique=True, blank=True)
    pub_date = models.DateTimeField('date published', auto_now_add=True)
    description = RichTextField(verbose_name='Описание', null=True, blank=True)
    created = models.DateTimeField(auto_now_add=True, verbose_name="Дата создания", null=True)
    updated = models.DateTimeField(auto_now=True, verbose_name="Дата обновления", null=True)

    def save(self, *args, **kwargs):
        self.news_slug = slugify(unidecode(self.title))
        super().save(*args, **kwargs)

    def __str__(self):
        return self.title

    class Meta:
        verbose_name = 'Новость'
        verbose_name_plural = 'Новости'
