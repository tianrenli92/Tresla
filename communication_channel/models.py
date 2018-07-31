from django.contrib.auth.models import User
from django.db import models
from project.models import Project


class Channel(models.Model):
    project = models.ForeignKey(Project, on_delete=models.CASCADE, related_name='channels')
    members = models.ManyToManyField(User, related_name='channels_joined')
    name = models.CharField(max_length=255)


class ChannelMessage(models.Model):
    sender = models.ForeignKey(User, on_delete=models.CASCADE, related_name='public_messages_sent')
    channel = models.ForeignKey(Channel, on_delete=models.CASCADE, related_name='messages')
    message = models.CharField(max_length=1200)
    timestamp = models.DateTimeField(auto_now_add=True)
    is_read = models.BooleanField(default=False)

    def __str__(self):
        return self.message

    class Meta:
        ordering = ('timestamp',)


class Message(models.Model):
    sender = models.ForeignKey(User, on_delete=models.CASCADE, related_name='messages_sent')
    receiver = models.ForeignKey(User, on_delete=models.CASCADE, related_name='messages_received')
    message = models.CharField(max_length=1200)
    timestamp = models.DateTimeField(auto_now_add=True)
    is_read = models.BooleanField(default=False)

    def __str__(self):
        return self.message

    class Meta:
        ordering = ('timestamp',)
