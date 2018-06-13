from django.contrib.auth.models import User
from django.db import models
from project.models import Project


class TaskList(models.Model):
    project = models.ForeignKey(Project, on_delete=models.CASCADE)
    name = models.CharField(max_length=255)
    timestamp = models.DateTimeField(auto_now_add=True)

    class Meta:
        ordering = ('project','timestamp',)

    def __str__(self):
        return self.name


class Task(models.Model):
    task_list = models.ForeignKey(TaskList, on_delete=models.CASCADE)
    topic = models.CharField(max_length=255)
    description = models.CharField(max_length=255)

    def __str__(self):
        return self.topic

