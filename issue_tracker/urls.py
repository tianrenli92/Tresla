from django.conf.urls import url
from django.urls import path
from . import views

app_name = 'issue_tracker'

urlpatterns =[
    path('',views.list_of_issue,name='list_of_issue'),
    path('<slug:slug>/',views.issue_detail,name='issue_detail'),
    path('project/<slug:project_slug>/',views.list_of_issue_by_project,name='list_of_issue_by_project'),
    path('<slug:slug>/comment',views.add_comment,name='add_comment'),
    path('issue/new_issue',views.new_issue,name='new_issue'),
]