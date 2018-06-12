from django.urls import include,path
from django.contrib.auth import views as auth_views
from . import views

app_name = 'project'

urlpatterns = [
    path('', views.project_list, name='project-list'),
    path('<int:project_id>/', views.project_detail, name='project-detail'),
    path('<int:project_id>/task/', include('task_tracker.urls')),
    path('<int:project_id>/issue/', include('issue_tracker.urls')),
    path('<int:project_id>/channel/', include('communication_channel.urls')),
]