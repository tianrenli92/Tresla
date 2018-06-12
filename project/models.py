from django.contrib.auth.models import User
from django.db import models
from django.urls import reverse


class Project(models.Model):
    name = models.CharField(max_length=255)
    owner = models.ForeignKey(User, on_delete=models.CASCADE, related_name='owner')
    timestamp = models.DateTimeField(auto_now_add=True)
    slug = models.SlugField(max_length=250, unique=True)

    class Meta:
        ordering = ('timestamp',)
        verbose_name = 'project'
        verbose_name_plural = 'projects'

    def get_absolute_url(self):
        return reverse('issue_tracker:list_of_issue_by_project', args=[self.slug])

    def __str__(self):
        return self.name


class ProjectMember(models.Model):
    project = models.ForeignKey(Project, on_delete=models.CASCADE, related_name='project_id')
    member = models.ForeignKey(User, on_delete=models.CASCADE, related_name='member')

    def __str__(self):
        return self.member.username

