from django.db import models
from django.utils.html import format_html
from django.utils.text import slugify

from googletrans import Translator

translator = Translator()

class Project(models.Model):
    title = models.CharField(max_length=255, verbose_name="Название проекта")
    description = models.TextField(verbose_name="Описание")
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
    project = models.ForeignKey(Project, on_delete=models.CASCADE, related_name="images")
    image = models.ImageField(upload_to="projects/images/", verbose_name="Фото")
    def image_tag(self):
        if self.image:
            return format_html('<img src="{}" width="100" height="100" style="object-fit: cover;"/>', self.image.url)
        return "Нет изображения"
    
    image_tag.short_description = "Превью"  # Заголовок в админке
    

class DocumentGroup(models.Model):
    name = models.CharField(max_length=255, verbose_name="Название проекта")

    class Meta:
            verbose_name = "Документ"
            verbose_name_plural = "Документы"

    def __str__(self):
        return self.name

class Document(models.Model):
    group = models.ForeignKey(DocumentGroup, on_delete=models.CASCADE, related_name="documents", verbose_name="Группа")
    file = models.FileField(upload_to="documents/", verbose_name="Файл")
    uploaded_at = models.DateTimeField(auto_now_add=True, verbose_name="Дата загрузки")

    class Meta:
            verbose_name = "Документ"
            verbose_name_plural = "Документы"

    def __str__(self):
        return self.file.name


