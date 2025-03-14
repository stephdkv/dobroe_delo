from django.contrib import admin

from django.contrib import admin
from django.contrib.auth.models import Group, User
from .models import Project, ProjectImage, Document, DocumentGroup, Sponsor, DocumentMain

class ProjectImageInline(admin.TabularInline):
    model = ProjectImage
    readonly_fields = ("image_tag",)  # Показываем превью внутри карточки
    extra = 1
    verbose_name = "Изображение проекта"
    verbose_name_plural = "Изображения проекта"

class DocumentInline(admin.TabularInline):  # Или StackedInline для другого вида
    model = Document
    extra = 1  # Количество пустых полей для загрузки новых документов
    fields = ('file',)  # Поля, которые можно редактировать
    verbose_name = "Документ"
    verbose_name_plural = "Документы"

class ProjectAdmin(admin.ModelAdmin):
    list_display = ('title', 'description')
    list_display_links = ('title',)
    search_fields = ('title',)
    inlines = [ProjectImageInline, DocumentInline]

    class Meta:
            verbose_name = "Проект"
            verbose_name_plural = "Проекты"

class DocumentInlineMain(admin.TabularInline):  # Позволяет загружать файлы в группе
    model = DocumentMain
    extra = 1  # Количество пустых форм для загрузки


class DocumentGroupAdmin(admin.ModelAdmin):
    list_display = ("name",)
    inlines = [DocumentInlineMain]  # Встраиваем форму загрузки файлов в группу

class SponsorAdmin(admin.ModelAdmin):
    list_display = ("name", "logo_tag", "website")  # Теперь отображается ссылка
    readonly_fields = ("logo_tag",)  # Показываем превью внутри карточки

admin.site.register(Sponsor, SponsorAdmin)

admin.site.register(DocumentGroup, DocumentGroupAdmin)
admin.site.register(Project, ProjectAdmin)
admin.site.unregister(User)
admin.site.unregister(Group)
admin.site.site_header = "Администрирование Доброе Дело"
admin.site.site_title = "Администрирование сайта Доброе Дело"





