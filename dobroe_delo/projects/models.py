from django.db import models

from django.db import models

class Project(models.Model):
    title = models.CharField(max_length=200, verbose_name="Название проекта")
    description = models.TextField(verbose_name="Описание проекта")
    image = models.ImageField(upload_to='projects/', verbose_name="Изображение")
    link = models.URLField(max_length=300, verbose_name="Ссылка на страницу проекта")

    def __str__(self):
        return self.title

    class Meta:
        verbose_name = "Проект"
        verbose_name_plural = "Проекты"

