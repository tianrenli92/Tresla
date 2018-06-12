from django.urls import path
from . import views

app_name = 'communication_channel'

urlpatterns = [
<<<<<<< HEAD
<<<<<<< HEAD
    path('communication_channel', views.channel_view, name='channel'),
=======
    path('', views.channel_list, name='channel_list'),
>>>>>>> 6709944bde6a76bb5f0e1917059e69c4b1e08110
=======
    path('communication_channel', views.channel_view, name='chats'),
>>>>>>> parent of 74c02b5... html change
    # URL form : "/api/messages/1/2"
    path('api/messages/<int:sender>/<int:receiver>', views.message_list, name='message-detail'),  # For GET request.
    # URL form : "/api/messages/"
    path('api/messages/', views.message_list, name='message-list'),   # For POST
    # URL form "/api/users/1"
    path('api/users/<int:pk>', views.user_list, name='user-detail'),      # GET request for user with id
    path('api/users/', views.user_list, name='user-list'),    # POST for new user and GET for all users list
]