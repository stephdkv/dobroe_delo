from django.contrib import admin

from django.contrib import admin
from .models import Project

@admin.register(Project)
class ProjectAdmin(admin.ModelAdmin):
    list_display = ('title', 'description', 'link')
    list_display_links = ('title',)
    search_fields = ('title',)

