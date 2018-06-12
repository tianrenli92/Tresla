from django.shortcuts import render


def task_group_list(request, project_id):

    return render(request, 'task_tracker/task_list.html', {'project_id':project_id})
