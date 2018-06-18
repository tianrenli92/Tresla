from django.urls import path
from . import views

app_name = 'communication_channel'

urlpatterns = [

    path('', views.channel_index, name='channel_index'),
    path('<int:channel_id>/', views.channel_view, name='channel_view'),
]