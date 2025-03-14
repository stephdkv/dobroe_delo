from django.db import models
from django.utils.html import format_html
from django.utils.text import slugify
import os

from googletrans import Translator

translator = Translator()

class Project(models.Model):
    title = models.CharField(max_length=255, verbose_name="Название проекта")
    description = models.TextField(blank=True, null=True, verbose_name="Описание")
    slug = models.SlugField(unique=True, blank=True, editable=False)  # Поле заполняется автоматически
    
    def save(self, *args, **kwargs):
        if not self.slug:  # Генерируем slug только если он не установлен
            translated_title = translator.translate(self.title, src='ru', dest='en').text  # Переводим название
            self.slug = slugify(translated_title)  # Преобразуем в slug
        super().save(*args, **kwargs)

    def get_absolute_url(self):
        return f"/projects/{self.slug}/"  # Генерируем ссылку на проект

    def __str__(self):
        return self.title
    
    class Meta:
        verbose_name = "Проект"
        verbose_name_plural = "Проекты"

class ProjectImage(models.Model):
    DEFAULT_IMAGE = "projects/images/default.png"  # Путь к дефолтному изображению
    project = models.ForeignKey(Project, on_delete=models.CASCADE, related_name="images")
    image = models.ImageField(upload_to="projects/images/",null=True, verbose_name="Фото")
    def image_tag(self):
        if self.image:  # Если изображение загружено → показываем его
            return format_html('<img src="{}" width="100" height="100" style="object-fit: cover;"/>', self.image.url)
        return format_html('<img src="{}" width="100" height="100" style="object-fit: cover;"/>', self.DEFAULT_IMAGE)

    image_tag.short_description = "Превью"  # Заголовок в админке

    def save(self, *args, **kwargs):
        if not self.image:  # Если изображение не загружено, устанавливаем дефолтное
            self.image = self.DEFAULT_IMAGE
        super().save(*args, **kwargs)  
    

class Document(models.Model):
    project = models.ForeignKey(Project, on_delete=models.CASCADE, related_name="documents", verbose_name="Проект", null=True, blank=True)  
    file = models.FileField(upload_to="documents/", verbose_name="Файл")
    uploaded_at = models.DateTimeField(auto_now_add=True, verbose_name="Дата загрузки")

    class Meta:
        verbose_name = "Документ"
        verbose_name_plural = "Документы"
    
    @property
    def short_name(self):
        return os.path.basename(self.file.name) 

    def __str__(self):
        return f"{self.project.title} - {self.file.name}"
    
class DocumentGroup(models.Model):
    name = models.CharField(max_length=255, verbose_name="Название группы документов")

    class Meta:
            verbose_name = "Документ"
            verbose_name_plural = "Документы"

    def __str__(self):
        return self.name

class DocumentMain(models.Model):
    group = models.ForeignKey(DocumentGroup, on_delete=models.CASCADE, related_name="documents", verbose_name="Группа")
    file = models.FileField(upload_to="documents/", verbose_name="Файл")
    uploaded_at = models.DateTimeField(auto_now_add=True, verbose_name="Дата загрузки")

    class Meta:
            verbose_name = "Документ"
            verbose_name_plural = "Документы"

class Sponsor(models.Model):
    name = models.CharField(max_length=255, verbose_name="Название партнера")
    logo = models.ImageField(upload_to="sponsors/logos/", verbose_name="Логотип")
    website = models.URLField(blank=True, null=True, verbose_name="Сайт партнера")

    def logo_tag(self):
        """ Отображение миниатюры логотипа в админке с кликабельной ссылкой """
        if self.logo:
            if self.website:
                return format_html('<a href="{}" target="_blank"><img src="{}" width="100" height="100" style="object-fit: cover;"/></a>', self.website, self.logo.url)
            return format_html('<img src="{}" width="100" height="100" style="object-fit: cover;"/>', self.logo.url)
        return "Нет изображения"

    logo_tag.short_description = "Превью"

    def __str__(self):
        return self.name

    class Meta:
        verbose_name = "Партнера"
        verbose_name_plural = "Партнеры"


