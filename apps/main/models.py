from django.db import models
from unidecode import unidecode
from django.utils.text import slugify
from ckeditor.fields import RichTextField


class AboutCompany(models.Model):
    title = models.CharField(max_length=255, verbose_name='Название')
    about_company_slug = models.SlugField(unique=True, blank=True)
    image = models.ImageField(upload_to='about_company_image/', verbose_name='Фотография')
    description = RichTextField(verbose_name='Описание')
    created = models.DateTimeField(auto_now_add=True, verbose_name="Дата создания", null=True)
    updated = models.DateTimeField(auto_now=True, verbose_name="Дата обновления", null=True)

    def save(self, *args, **kwargs):
        self.about_company_slug = slugify(unidecode(self.title))
        super().save(*args, **kwargs)

    def __str__(self):
        return self.title

    class Meta:
        verbose_name = 'О Компании'
        verbose_name_plural = 'О Компании'


class OurExperience(models.Model):
    title = models.CharField(max_length=255, verbose_name='Название')
    our_experience_slug = models.SlugField(unique=True, blank=True)
    image = models.ImageField(upload_to='our_experience_image/', verbose_name='Фотография')
    description = RichTextField(verbose_name='Описание')
    created = models.DateTimeField(auto_now_add=True, verbose_name="Дата создания", null=True)
    updated = models.DateTimeField(auto_now=True, verbose_name="Дата обновления", null=True)

    def save(self, *args, **kwargs):
        self.our_experience_slug = slugify(unidecode(self.title))
        super().save(*args, **kwargs)

    def __str__(self):
        return self.title

    class Meta:
        verbose_name = 'Наш опыт'
        verbose_name_plural = 'Наши опыты'


class OurCommandProfession(models.Model):
    title = models.CharField(max_length=255, verbose_name='Название')
    our_command_profession_slug = models.SlugField(unique=True, blank=True)
    description = models.TextField(verbose_name='Описание')
    created = models.DateTimeField(auto_now_add=True, verbose_name="Дата создания", null=True)
    updated = models.DateTimeField(auto_now=True, verbose_name="Дата обновления", null=True)

    def save(self, *args, **kwargs):
        self.our_command_profession_slug = slugify(unidecode(self.title))
        super().save(*args, **kwargs)

    def __str__(self):
        return self.title

    class Meta:
        verbose_name = 'Специальность нашей команды'
        verbose_name_plural = 'Специальности нашей команды'


class OurCommand(models.Model):
    title = models.CharField(max_length=255, verbose_name='Название')
    our_command_slug = models.SlugField(unique=True, blank=True)
    description = models.TextField(verbose_name='Описание')
    profession = models.ForeignKey(OurCommandProfession, on_delete=models.DO_NOTHING, null=True, blank=True,
                                   verbose_name='Специальность')
    created = models.DateTimeField(auto_now_add=True, verbose_name="Дата создания", null=True)
    updated = models.DateTimeField(auto_now=True, verbose_name="Дата обновления", null=True)

    def save(self, *args, **kwargs):
        self.our_command_slug = slugify(unidecode(self.title))
        super().save(*args, **kwargs)

    def __str__(self):
        return self.title

    class Meta:
        verbose_name = 'Наша Команда'
        verbose_name_plural = 'Наша Команда'


class Vacancy(models.Model):
    title = models.CharField(max_length=255, verbose_name='Название')
    vacancy_slug = models.SlugField(unique=True, blank=True)
    requirements = RichTextField(verbose_name='Требования')
    responsibilities = RichTextField(verbose_name='Обязанности')
    conditions = RichTextField(verbose_name='Условия')
    pub_date = models.DateTimeField('Дата публикации', auto_now_add=True, null=True)
    created = models.DateTimeField(auto_now_add=True, verbose_name="Дата создания", null=True)
    updated = models.DateTimeField(auto_now=True, verbose_name="Дата обновления", null=True)

    def save(self, *args, **kwargs):
        self.vacancy_slug = slugify(unidecode(self.title))
        super().save(*args, **kwargs)

    def __str__(self):
        return self.title

    class Meta:
        verbose_name = 'Вакансия'
        verbose_name_plural = 'Вакансии'
