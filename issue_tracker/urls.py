from django.conf.urls import url
from django.urls import path
from . import views

app_name = 'issue_tracker'

urlpatterns =[
    path('',views.list_of_issue,name='list_of_issue'),
    path('<int:issue_id>/',views.issue_detail,name='issue_detail'),
    path('<int:issue_id>/comment',views.add_comment,name='add_comment'),
    path('new_issue/',views.new_issue,name='new_issue'),
    path('<int:issue_id>/edit_issue/',views.edit_issue,name='edit_issue'),
]