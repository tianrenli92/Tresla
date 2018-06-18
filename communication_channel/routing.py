from django.conf.urls import url

from . import consumers

websocket_urlpatterns = [
    url(r'^ws/project/{{ project_id }}/channel/(?P<room_name>[^/]+)/$', consumers.CommunicationConsumer),
]