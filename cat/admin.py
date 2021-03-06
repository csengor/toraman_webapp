from django.contrib import admin

from .models import Project, ProjectFile, TranslationMemory
# Register your models here.

class ProjectAdmin(admin.ModelAdmin):
    list_display = ('title', 'source_language', 'target_language', 'created_by')

admin.site.register(Project, ProjectAdmin)

class ProjectFileAdmin(admin.ModelAdmin):
    list_display = ('title', 'translator', 'created_by', 'project')

admin.site.register(ProjectFile, ProjectFileAdmin)

class TranslationMemoryAdmin(admin.ModelAdmin):
    list_display = ('title', 'source_language', 'target_language', 'user')

admin.site.register(TranslationMemory, TranslationMemoryAdmin)
