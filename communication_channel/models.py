from django.db import models
from django.contrib.auth.models import User
from project.models import Project


class Channel(models.Model):
    project = models.ForeignKey(Project, on_delete=models.CASCADE)
    owner = models.ForeignKey(User, on_delete=models.CASCADE)
    name = models.CharField(max_length=255)


class ChannelMember(models.Model):
    channel = models.ForeignKey(Channel, on_delete=models.CASCADE)
    member = models.ForeignKey(User, on_delete=models.CASCADE)