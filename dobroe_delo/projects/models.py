from django.db import models
from django.utils.text import slugify

from googletrans import Translator

translator = Translator()

class Project(models.Model):
    title = models.CharField(max_length=255)
    description = models.TextField()
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
    image = models.ImageField(upload_to="projects/images/")
    
    
