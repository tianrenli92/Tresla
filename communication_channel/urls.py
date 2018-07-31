from django.contrib.auth.views import logout
from django.urls import path
from . import views

app_name = 'communication_channel'
urlpatterns = [
    path('', views.channel_index, name='channel_index'),
    path('<int:channel_id>/', views.channel_view, name='channel_view'),
    path('<int:channel_id>/channel_message_list/', views.channel_message_list, name='channel_message_list'),
    path('message/<int:target_id>/', views.message_view, name='message_view'),
    path('message_list/', views.message_list, name='message_list'),
]
