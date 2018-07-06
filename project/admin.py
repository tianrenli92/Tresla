from django.contrib import admin
from .models import Project,ProjectMember


class ProjectAdmin(admin.ModelAdmin):
    list_display = ('name', 'owner', 'timestamp')


class ProjectMemberAdmin(admin.ModelAdmin):
    list_display = ('member','project')


admin.site.register(Project,ProjectAdmin)
admin.site.register(ProjectMember,ProjectMemberAdmin)
