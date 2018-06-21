from django.conf.urls import url

from . import consumers

websocket_urlpatterns = [
    url(r'^ws/project/(?P<project_id>[^/]+)/channel/(?P<channel_id>[^/]+)/$', consumers.CommunicationConsumer),
]