from django.db import models
from ckeditor.fields import RichTextField
from unidecode import unidecode
from django.utils.text import slugify


class Region(models.Model):
    title = models.CharField('название региона', max_length=255)
    region_slug = models.SlugField(unique=True, blank=True)

    def save(self, *args, **kwargs):
        self.region_slug = slugify(unidecode(self.title))
        super().save(*args, **kwargs)

    def __str__(self):
        return self.title

    class Meta:
        verbose_name = 'Регион'
        verbose_name_plural = 'Регионы'


class AnalysisCategory(models.Model):
    region = models.ForeignKey(Region, on_delete=models.DO_NOTHING, verbose_name="Регион")
    category_name = models.CharField('Категорий анализа', max_length=255)
    analysis_category_slug = models.SlugField(unique=True, blank=True)
    category_description = models.TextField(verbose_name="Описание Категория")
    created = models.DateTimeField(auto_now_add=True, verbose_name="Дата создания", null=True)
    updated = models.DateTimeField(auto_now=True, verbose_name="Дата обновления", null=True)

    def save(self, *args, **kwargs):
        self.analysis_category_slug = slugify(unidecode(self.category_name))
        super().save(*args, **kwargs)

    def __str__(self):
        return f'{self.category_name} '

    class Meta:
        verbose_name = 'Категорий анализа'
        verbose_name_plural = 'Категории анализов'


class Analysis(models.Model):
    analyse_category = models.ForeignKey(AnalysisCategory, verbose_name='Категорий анализа', on_delete=models.DO_NOTHING
                                         , null=True, blank=False)
    analysis_name = models.CharField(max_length=255, verbose_name="Название анализа")
    analysis_slug = models.SlugField(unique=True, blank=True)
    analysis_description = models.TextField(verbose_name="Описание анализа")
    price = models.IntegerField(verbose_name="Цена")
    Patient_instructions = models.TextField(verbose_name="Инструкции для пациента")
    procedure_description = models.TextField(verbose_name="Описание процедуры")
    expected_results = models.TextField(verbose_name="Ожидаемые результаты")
    results_delivery_time = models.CharField(max_length=255, verbose_name="Время доставки результатов")
    sale = models.BooleanField(default=False, verbose_name="Распродажа")
    promotion = models.BooleanField(default=False, verbose_name="Акция")
    created = models.DateTimeField(auto_now_add=True, verbose_name="Дата создания", null=True)
    updated = models.DateTimeField(auto_now=True, verbose_name="Дата обновления", null=True)

    def save(self, *args, **kwargs):
        self.analysis_slug = slugify(unidecode(self.analysis_name))
        super().save(*args, **kwargs)

    def __str__(self):
        return self.analysis_name

    class Meta:
        verbose_name = 'Анализ'
        verbose_name_plural = 'Анализы'


class RehabilitationCategory(models.Model):
    region = models.ForeignKey(Region, on_delete=models.DO_NOTHING, verbose_name="Регион", null=True, blank=False)
    rehabilitation_category_name = models.CharField('Категорий реабилитации', max_length=100, blank=True)
    rehabilitation_category_slug = models.SlugField(unique=True, blank=True)
    created = models.DateTimeField(auto_now_add=True, verbose_name="Дата создания", null=True)
    updated = models.DateTimeField(auto_now=True, verbose_name="Дата обновления", null=True)

    def save(self, *args, **kwargs):
        self.rehabilitation_category_slug = slugify(unidecode(self.rehabilitation_category_name))
        super().save(*args, **kwargs)

    def __str__(self):
        return self.rehabilitation_category_name

    class Meta:
        verbose_name = 'Категорий реабилитации'
        verbose_name_plural = 'Категории реабилитации'


class Rehabilitation(models.Model):
    rehabilitation_category = models.ForeignKey(
        RehabilitationCategory, verbose_name='Категории реабилитации', on_delete=models.DO_NOTHING,
        blank=True, null=True, related_name='rehab_cat'
    )
    rehabilitation_name = models.CharField(max_length=100, verbose_name='Название реабилитации')
    rehabilitation_slug = models.SlugField(unique=True, blank=True)
    image = models.ImageField(upload_to='image_rehabilitation/', verbose_name='Изображение')
    rehabilitation_description = models.TextField(verbose_name='Описание реабилитации')
    created = models.DateTimeField(auto_now_add=True, verbose_name="Дата создания", null=True)
    updated = models.DateTimeField(auto_now=True, verbose_name="Дата обновления", null=True)

    def save(self, *args, **kwargs):
        self.rehabilitation_slug = slugify(unidecode(self.rehabilitation_name))
        super().save(*args, **kwargs)

    def __str__(self):
        return self.rehabilitation_name

    class Meta:
        verbose_name = 'Реабилитация'
        verbose_name_plural = 'Реабилитации'


class DiagnosticCategory(models.Model):
    region = models.ForeignKey(Region, on_delete=models.DO_NOTHING, blank=True, null=True, verbose_name='Регион')
    diagnostic_category_name = models.CharField(max_length=100, blank=True,
                                                verbose_name='Название категории диагностики')
    diagnostic_category_slug = models.SlugField(unique=True, blank=True)
    created = models.DateTimeField(auto_now_add=True, verbose_name="Дата создания", null=True)
    updated = models.DateTimeField(auto_now=True, verbose_name="Дата обновления", null=True)

    def save(self, *args, **kwargs):
        self.diagnostic_category_slug = slugify(unidecode(self.diagnostic_category_name))
        super().save(*args, **kwargs)

    def __str__(self):
        return self.diagnostic_category_name

    class Meta:
        verbose_name = 'категорий диагностики'
        verbose_name_plural = 'Категории диагностики'


class DiagnosticSubcategory(models.Model):
    diagnostic_category = models.ForeignKey(
        DiagnosticCategory, on_delete=models.DO_NOTHING, blank=True, null=True,
        verbose_name='Категория диагностики'
    )
    diagnostic_subcategory_name = models.CharField(
        max_length=100, verbose_name='Название подкатегории диагностики'
    )
    diagnostic_subcategory_slug = models.SlugField(unique=True, blank=True)

    diagnostic_subcategory_description = models.TextField(
        verbose_name='Описание подкатегории диагностики'
    )
    image = models.ImageField(
        upload_to='image_diagnostic/', verbose_name='Изображение'
    )
    created = models.DateTimeField(auto_now_add=True, verbose_name="Дата создания", null=True)
    updated = models.DateTimeField(auto_now=True, verbose_name="Дата обновления", null=True)

    def save(self, *args, **kwargs):
        self.diagnostic_subcategory_slug = slugify(unidecode(self.diagnostic_subcategory_name))
        super().save(*args, **kwargs)

    def __str__(self):
        return self.diagnostic_subcategory_name

    class Meta:
        verbose_name = 'Подкатегория диагностики'
        verbose_name_plural = 'Подкатегории диагностики'


class Diagnostic(models.Model):
    diagnostic_subcategory = models.ForeignKey(
        DiagnosticSubcategory, on_delete=models.DO_NOTHING, blank=True, null=True,
        verbose_name='Подкатегория диагностики'
    )
    diagnostic_name = models.CharField(
        max_length=100, verbose_name='Название диагностики'
    )
    diagnostic_slug = models.SlugField(unique=True, blank=True)
    image = models.ImageField(
        upload_to='image_diagnostic/', verbose_name='Изображение'
    )
    description = models.TextField(
        verbose_name='Описание'
    )
    sale = models.BooleanField(default=False, verbose_name='Распродажа')
    promotion = models.BooleanField(default=False, verbose_name='Акция')
    created = models.DateTimeField(auto_now_add=True, verbose_name="Дата создания", null=True)
    updated = models.DateTimeField(auto_now=True, verbose_name="Дата обновления", null=True)

    def save(self, *args, **kwargs):
        self.diagnostic_slug = slugify(unidecode(self.diagnostic_name))
        super().save(*args, **kwargs)

    def __str__(self):
        return self.diagnostic_name

    class Meta:
        verbose_name = 'Диагностика'
        verbose_name_plural = 'Диагностики'


class PolyclinicCategory(models.Model):
    region = models.ForeignKey(
        Region, on_delete=models.DO_NOTHING, blank=True, null=True,
        verbose_name='Регион'
    )
    polyclinic_category_name = models.CharField(
        max_length=100, blank=True, verbose_name='Название категории поликлиники'
    )
    polyclinic_category_slug = models.SlugField(unique=True, blank=True)

    created = models.DateTimeField(auto_now_add=True, verbose_name="Дата создания", null=True)
    updated = models.DateTimeField(auto_now=True, verbose_name="Дата обновления", null=True)

    def save(self, *args, **kwargs):
        self.polyclinic_category_slug = slugify(unidecode(self.polyclinic_category_name))
        super().save(*args, **kwargs)

    def __str__(self):
        return self.polyclinic_category_name

    class Meta:
        verbose_name = 'категорий поликлиники'
        verbose_name_plural = 'Категории поликлиники'


class Polyclinic(models.Model):
    polyclinic_category = models.ForeignKey(
        PolyclinicCategory, on_delete=models.DO_NOTHING, blank=True, null=True,
        verbose_name='Категория поликлиники'
    )
    polyclinic_name = models.CharField(
        max_length=100, verbose_name='Название поликлиники'
    )
    polyclinic_slug = models.SlugField(unique=True, blank=True)

    price_first_meet = models.IntegerField(
        verbose_name='Цена первичной встречи'
    )
    price_second_meet = models.IntegerField(
        verbose_name='Цена повторной встречи'
    )
    about_service = RichTextField(
        verbose_name='Описание услуг'
    )
    about_procedure = RichTextField(
        verbose_name='Описание процедур'
    )
    created = models.DateTimeField(auto_now_add=True, verbose_name="Дата создания", null=True)
    updated = models.DateTimeField(auto_now=True, verbose_name="Дата обновления", null=True)

    def save(self, *args, **kwargs):
        self.polyclinic_slug = slugify(unidecode(self.polyclinic_name))
        super().save(*args, **kwargs)

    def __str__(self):
        return self.polyclinic_name

    class Meta:
        verbose_name = 'Поликлиника'
        verbose_name_plural = 'Поликлиники'


class AddressCenter(models.Model):
    title = models.CharField(max_length=255, verbose_name='Заголовок')
    address_center_slug = models.SlugField(unique=True, blank=True)
    description = RichTextField(verbose_name='Полное описание')
    created = models.DateTimeField(auto_now_add=True, verbose_name="Дата создания", null=True)
    updated = models.DateTimeField(auto_now=True, verbose_name="Дата обновления", null=True)

    def save(self, *args, **kwargs):
        self.address_center_slug = slugify(unidecode(self.title))
        super().save(*args, **kwargs)

    def __str__(self):
        return self.title

    class Meta:
        verbose_name = 'Центр-адрес'
        verbose_name_plural = 'Центры-адреса'
