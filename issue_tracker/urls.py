from django.conf.urls import url
from django.urls import path
from . import views
from django.views.generic import TemplateView

app_name = 'issue_tracker'

urlpatterns =[
    path('',views.list_of_issue,name='list_of_issue'),
    path('<int:issue_id>/',views.issue_detail,name='issue_detail'),
    path('<int:issue_id>/comment',views.add_comment,name='add_comment'),
    path('new_issue/',views.new_issue,name='new_issue'),
    path('<int:issue_id>/edit_issue/',views.edit_issue,name='edit_issue'),
    path('<int:issue_id>/delete_issue/',views.delete_issue,name='delete_issue'),
    path('<int:issue_id>/delete', TemplateView.as_view(template_name="issue_tracker/issue/nice_delete.html"), name='success_deletion'),
    path('<int:issue_id>/assignee/', views.assignee, name='assignee'),
    path('<int:issue_id>/statusissue/', views.statusissue, name='statusissue'),
    path('issues/',views.user_issues,name='user_issues'),

]
