from django.urls import path,re_path
from . import views

app_name = 'task_tracker'


urlpatterns = [
    path('', views.task_list_index, name='task_list_index'),
    path('task_list_create/', views.task_list_create, name='task_list_create'),
    path('<int:task_list_id>/delete/', views.task_list_delete, name='task_list_delete'),
    # path('<int:task_list_id>/update/', views.task_list_update, name='task_list_update'),
]