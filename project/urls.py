from django.urls import include,path
from django.contrib.auth import views as auth_views
from . import views
from django.views.generic import TemplateView

app_name = 'project'

urlpatterns = [
    path('', views.project_index, name='project_index'),
    path('<int:project_id>/', views.project_detail, name='project_detail'),
    path('create/', views.project_create, name='project_create'),
    path('<int:project_id>/delete/', views.project_delete, name='project_delete'),
    path('<int:project_id>/edit/', views.project_edit, name='project_edit'),

    path('<int:project_id>/task/', include('task_tracker.urls')),
    path('<int:project_id>/issue/', include('issue_tracker.urls',namespace='issue_tracker')),
    path('<int:project_id>/channel/', include('communication_channel.urls')),
    path('<int:issue_id>/delete', TemplateView.as_view(template_name="project/templates/project/nice_delete_project.html"), name='success_deletion_project'),
]