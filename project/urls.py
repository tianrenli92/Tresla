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
    path('<int:project_id>/delete_result/', TemplateView.as_view(template_name="project/delete_result.html"), name='delete_result'),
    path('<int:project_id>/edit/', views.project_edit, name='project_edit'),
    path('<int:project_id>/member_create/', views.project_member_create, name='project_member_create'),
    path('<int:project_id>/member_delete/', views.project_member_delete, name='project_member_delete'),

    path('<int:project_id>/task/', include('task_tracker.urls')),
    path('<int:project_id>/issue/', include('issue_tracker.urls')),
    path('<int:project_id>/channel/', include('communication_channel.urls', namespace='communication_channel')),
]