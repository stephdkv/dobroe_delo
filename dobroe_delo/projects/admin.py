from django.contrib import admin

from django.contrib import admin
from django.contrib.auth.models import Group, User
from .models import Project, ProjectImage, Document, DocumentGroup

class ProjectImageInline(admin.TabularInline):
    model = ProjectImage
    readonly_fields = ("image_tag",)  # Показываем превью внутри карточки
    extra = 1
    verbose_name = "Изображение проекта"
    verbose_name_plural = "Изображения проекта"

class ProjectAdmin(admin.ModelAdmin):
    list_display = ('title', 'description')
    list_display_links = ('title',)
    search_fields = ('title',)
    inlines = [ProjectImageInline]

    class Meta:
            verbose_name = "Проект"
            verbose_name_plural = "Проекты"

class DocumentInline(admin.TabularInline):  # Позволяет загружать файлы в группе
    model = Document
    extra = 1  # Количество пустых форм для загрузки

@admin.register(DocumentGroup)
class DocumentGroupAdmin(admin.ModelAdmin):
    list_display = ("name",)
    inlines = [DocumentInline]  # Встраиваем форму загрузки файлов в группу


admin.site.register(Project, ProjectAdmin)
admin.site.unregister(User)
admin.site.unregister(Group)
admin.site.site_header = "Администрирование Доброе Дело"
admin.site.site_title = "Администрирование сайта Доброе Дело"

