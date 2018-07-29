from django.contrib.auth.views import logout
from django.urls import path
from . import views

app_name = 'communication_channel'
urlpatterns = [
    path('', views.index, name='channel_index'),
    path('<int:target_id>/', views.message_view, name='chat'),
    path('message_list/', views.message_list, name='message_list'),
    path('api/users/<int:user_id>/', views.user_list, name='user_detail'),
    path('api/users/', views.user_list, name='user_list'),
]
