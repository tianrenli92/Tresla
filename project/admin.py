from django.contrib import admin
from .models import Project,ProjectMember

class ProjectAdmin(admin.ModelAdmin):
    list_display = ('name', 'slug')
    prepopulated_fields = {'slug': ('name',)}


admin.site.register(Project)
admin.site.register(ProjectMember)
