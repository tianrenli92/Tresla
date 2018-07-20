from django.contrib.auth.views import logout
from django.urls import path
from . import views

app_name = 'communication_channel'
urlpatterns = [
    path('', views.index, name='channel_index'),
    path('<int:sender_id>/<int:receiver_id>/', views.message_view, name='chat'),
    path('api/messages/<int:sender>/<int:receiver>/', views.message_list, name='message_detail'),
    path('api/messages/', views.message_list, name='message_list'),
    path('api/users/<int:pk>/', views.user_list, name='user_detail'),
    path('api/users/', views.user_list, name='user_list'),
]
