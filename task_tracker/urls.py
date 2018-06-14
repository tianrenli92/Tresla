from django.urls import path,re_path
from . import views

app_name = 'task_tracker'


urlpatterns = [
    path('', views.task_list_index, name='task_list_index'),
    path('task_list/create/', views.task_list_create, name='task_list_create'),
    path('task_list/<int:task_list_id>/update/', views.task_list_update, name='task_list_update'),
    path('task_list/<int:task_list_id>/delete/', views.task_list_delete, name='task_list_delete'),
    path('task_list/<int:task_list_id>/task/create/', views.task_create, name='task_create'),
    path('task_list/<int:task_list_id>/task/<int:task_id>/update/', views.task_update, name='task_update'),
    path('task_list/<int:task_list_id>/task/<int:task_id>/delete/', views.task_delete, name='task_delete'),
]