from django.contrib import admin
from .models import Channel,ChannelMessage,Message

# Register your models here.
admin.site.register(Channel)
admin.site.register(ChannelMessage)
admin.site.register(Message)
