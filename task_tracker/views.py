from django.shortcuts import render, get_object_or_404, redirect
from .models import Project, TaskList, TaskListForm, Task, TaskForm
from django.http import Http404


def task_list_index(request, project_id):
    project = Project.objects.get(id=project_id)
    task_list_list = TaskList.objects.filter(project_id=project_id)
    return render(request, 'task_tracker/task_list_index.html',
                  {'project': project, 'task_list_list': task_list_list})


def task_list_create(request, project_id):
    project = Project.objects.get(id=project_id)
    if request.method == 'POST':
        task_list = TaskList(project_id=project_id)
        form = TaskListForm(request.POST, instance=task_list)
        if form.is_valid():
            form.save()
        return redirect('project:task_tracker:task_list_index', project_id=project_id)

    else:
        form = TaskListForm()
        return render(request, 'task_tracker/task_list_create.html', {'project': project, 'form': form})


def task_list_update(request, project_id, task_list_id):
    project = Project.objects.get(id=project_id)
    try:
        task_list = TaskList.objects.get(id=task_list_id)
    except TaskList.DoesNotExist:
        raise Http404("No such task list.")

    if request.method == 'POST':
        form = TaskListForm(request.POST, instance=task_list)
        if form.is_valid():
            form.save()
        return redirect('project:task_tracker:task_list_index', project_id=project_id)

    else:
        form = TaskListForm(instance=task_list)
        return render(request, 'task_tracker/task_list_create.html', {'project': project, 'form': form})


def task_list_delete(request, project_id, task_list_id):
    try:
        instance = TaskList.objects.get(id=task_list_id)
    except TaskList.DoesNotExist:
        raise Http404("No such task list.")
    instance.delete()
    return redirect('project:task_tracker:task_list_index', project_id=project_id)


def task_create(request, project_id, task_list_id):
    project = Project.objects.get(id=project_id)
    if request.method == 'POST':
        form = TaskForm(request.POST)
        if form.is_valid():
            form.save()
        return redirect('project:task_tracker:task_list_index', project_id=project_id)

    else:
        form = TaskForm(initial={'task_list': task_list_id})
        return render(request, 'task_tracker/task_create.html',
                      {'project': project, 'task_list_id': task_list_id, 'form': form})


def task_update(request, project_id, task_list_id, task_id):
    project = Project.objects.get(id=project_id)
    try:
        task = Task.objects.get(id=task_id)
    except TaskList.DoesNotExist:
        raise Http404("No such task.")

    if request.method == 'POST':
        form = TaskForm(request.POST, instance=task)
        if form.is_valid():
            form.save()
        return redirect('project:task_tracker:task_list_index', project_id=project_id)

    else:
        form = TaskForm(instance=task)
        return render(request, 'task_tracker/task_create.html',
                      {'project': project, 'task_list_id': task_list_id,'task_id': task_id, 'form': form})


def task_delete(request, project_id, task_list_id, task_id):
    try:
        instance = Task.objects.get(id=task_id)
    except TaskList.DoesNotExist:
        raise Http404("No such task.")
    instance.delete()
    return redirect('project:task_tracker:task_list_index', project_id=project_id)
