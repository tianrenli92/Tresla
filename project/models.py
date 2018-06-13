from django.contrib.auth.models import User
from django.db import models
from django.urls import reverse


class Project(models.Model):
    owner = models.ForeignKey(User, on_delete=models.CASCADE)
    name = models.CharField(max_length=255)
    timestamp = models.DateTimeField(auto_now_add=True)

    class Meta:
        ordering = ('timestamp',)

    def get_absolute_url(self):
        return reverse('project:project-detail', args=[self.id])

    def __str__(self):
        return self.name


class ProjectMember(models.Model):
    project = models.ForeignKey(Project, on_delete=models.CASCADE)
    member = models.ForeignKey(User, on_delete=models.CASCADE)

    class Meta:
        ordering = ('project','member',)

    def __str__(self):
        return self.member.username

