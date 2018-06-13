from django.shortcuts import render,get_list_or_404
from .models import Project,TaskList


def task_group_list(request, project_id):
    task_list_list=get_list_or_404(TaskList, project_id=project_id)
    print(task_list_list)
    return render(request, 'task_tracker/task_list_list.html', {'project_id':project_id, 'task_list_list':task_list_list})
