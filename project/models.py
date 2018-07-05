from django.contrib.auth.models import User
from django.db import models
from django.urls import reverse
from django.forms import ModelForm


class Project(models.Model):
    owner = models.ForeignKey(User, on_delete=models.CASCADE, related_name='owned_projects')
    name = models.CharField(max_length=10)
    timestamp = models.DateTimeField(auto_now_add=True)

    class Meta:
        ordering = ('timestamp',)

    def get_absolute_url(self):
        return reverse('project:project_detail', args=[self.id])

    def __str__(self):
        return self.name


class ProjectMember(models.Model):
    project = models.ForeignKey(Project, on_delete=models.CASCADE, related_name='members')
    member = models.ForeignKey(User, on_delete=models.CASCADE, related_name='joined_projects')

    class Meta:
        ordering = ('project','member',)

    def __str__(self):
        return self.member.username



class ProjectForm(ModelForm):
    class Meta:
        model=Project
        fields = ['name']

class UserSerializer:
    class Meta:
        model = User
        fields = ('pk', 'username')
    def create(self,validated_data):
        return User(**validated_data)