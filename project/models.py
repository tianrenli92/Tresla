from django.contrib.auth.models import User
from django.db import models
from django.urls import reverse
from django.forms import ModelForm


class Project(models.Model):
    owner = models.ForeignKey(User, on_delete=models.CASCADE, related_name='projects_owned')
    members= models.ManyToManyField(User, related_name='projects_joined')
    name = models.CharField(max_length=10)
    timestamp = models.DateTimeField(auto_now_add=True)

    class Meta:
        ordering = ('timestamp',)

    def get_absolute_url(self):
        return reverse('project:project_detail', args=[self.id])

    def __str__(self):
        return self.name

class ProjectForm(ModelForm):
    class Meta:
        model=Project
        fields = ['name']
