from django.urls import path,re_path
from . import views

app_name = 'task_tracker'


urlpatterns = [
    path('', views.task_group_list, name='task_group_list'),
]