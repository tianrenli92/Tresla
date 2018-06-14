from django.urls import include,path
from django.contrib.auth import views as auth_views
from . import views

app_name = 'project'

urlpatterns = [
    path('', views.project_index, name='project_index'),
    path('<int:project_id>/', views.project_detail, name='project_detail'),
    path('create/', views.project_create, name='project_create'),
    # path('delete/', views.project_delete, name='project_delete'),
    # path('update/', views.project_update, name='project_update'),

    path('<int:project_id>/task/', include('task_tracker.urls')),
    path('<int:project_id>/issue/', include('issue_tracker.urls',namespace='issue_tracker')),
    path('<int:project_id>/channel/', include('communication_channel.urls')),
]