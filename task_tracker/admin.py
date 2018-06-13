from django.contrib import admin
from .models import TaskList,Task


class TaskListAdmin(admin.ModelAdmin):
    list_display = ('name','project')


class TaskAdmin(admin.ModelAdmin):
    list_display = ('topic','description','task_list')


admin.site.register(TaskList,TaskListAdmin)
admin.site.register(Task,TaskAdmin)
