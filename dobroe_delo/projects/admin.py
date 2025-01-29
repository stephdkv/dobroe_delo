from django.contrib import admin

from django.contrib import admin
from .models import Project, ProjectImage

class ProjectImageInline(admin.TabularInline):
    model = ProjectImage
    extra = 1
    verbose_name = "Изображение проекта"
    verbose_name_plural = "Изображения проекта"

class ProjectAdmin(admin.ModelAdmin):
    list_display = ('title', 'description', 'slug')
    list_display_links = ('title',)
    search_fields = ('title',)
    inlines = [ProjectImageInline]

    class Meta:
            verbose_name = "Проект"
            verbose_name_plural = "Проекты"


admin.site.register(Project, ProjectAdmin)

