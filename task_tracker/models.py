from django.contrib.auth.models import User
from django.db import models
from django import forms
from django.forms import ModelForm
from project.models import Project


class TaskList(models.Model):
    project = models.ForeignKey(Project, on_delete=models.CASCADE)
    name = models.CharField(max_length=255)
    timestamp = models.DateTimeField(auto_now_add=True)

    class Meta:
        ordering = ('project','timestamp',)

    def __str__(self):
        return self.name


class TaskListForm(ModelForm):
    class Meta:
        model=TaskList
        fields = ['name']


class Task(models.Model):
    task_list = models.ForeignKey(TaskList, on_delete=models.CASCADE, related_name='tasks')
    topic = models.CharField(max_length=255)
    description = models.CharField(max_length=255)

    def __str__(self):
        return self.topic


class TaskForm(ModelForm):
    description = forms.CharField(required=False, widget=forms.Textarea(attrs={'cols': 50, 'rows': 10}))

    class Meta:
        model=Task
        fields = ['task_list','topic','description']

