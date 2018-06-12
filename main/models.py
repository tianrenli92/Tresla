from django.db import models

# Create your models here.

from django.contrib.auth.models import User
from django.db import models


class Project(models.Model):
    name = models.CharField(max_length=1200)
    owner = models.ForeignKey(User, on_delete=models.CASCADE, related_name='owner')
    timestamp = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return self.name

    class Meta:
        ordering = ('timestamp',)


class ProjectMember(models.Model):
    project = models.ForeignKey(Project, on_delete=models.CASCADE, related_name='project_id')
    member = models.ForeignKey(User, on_delete=models.CASCADE, related_name='member')

    def __str__(self):
        return self.member.username

