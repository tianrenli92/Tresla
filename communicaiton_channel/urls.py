from django.urls import path
from . import views

app_name = 'communicaiton_channel'

urlpatterns = [

    path('', views.channel_index, name='channel'),
    path('<int:channel_id>/', views.channel_view, name='room'),
]