from django.shortcuts import render, get_list_or_404, redirect, get_object_or_404
from .models import Project, ProjectForm
from django.contrib.auth.models import User
from django.http import Http404, HttpResponse
from rest_framework import generics
from rest_framework.renderers import JSONRenderer
from rest_framework.parsers import JSONParser
from django.http import HttpResponse, JsonResponse
from django.views.decorators.csrf import csrf_exempt


def project_index(request):
    user=request.user
    owned_project = [x for x in user.projects_owned.all()]
    joined_project = [x for x in user.projects_joined.all()]
    project_list=owned_project+joined_project
    return render(request, 'project/project_index.html', {'project_list': project_list})


def project_detail(request, project_id):
    users = User.objects.all()
    project = Project.objects.get(id=project_id)
    return render(request, 'project/project_detail.html',
                  {'project': project, 'users': users})


def project_create(request):
    if request.method == 'POST':
        project = Project(owner_id=request.user.id)
        form = ProjectForm(request.POST, instance=project)
        if form.is_valid():
            form.save()
        return redirect('project:project_index')

    else:
        form = ProjectForm()
        return render(request, 'project/project_create.html', {'form': form})


def project_delete(request, project_id):
    try:
        instance = Project.objects.get(id=project_id)
    except Project.DoesNotExist:
        raise Http404("No such project.")
    instance.delete()
    return redirect('project:project_index')


def project_edit(request, project_id):
    project = get_object_or_404(Project, id=project_id)
    form = ProjectForm(request.POST or None, instance=project)
    if form.is_valid():
        form.save()
        return redirect('project:project_detail', project_id=project_id)
    return render(request, 'project/project_edit.html', {'form': form})


@csrf_exempt
def project_member_create(request, project_id):
    if request.method == 'POST':
        try:
            project = Project.objects.get(id=project_id)
        except Project.DoesNotExist:
            raise Http404("No such project.")

        user_id = request.POST.get('user_id', None)
        user = User.objects.get(id=user_id)
        if user_id != str(project.owner.id):
            project.members.add(user)
            project.save()
        return JsonResponse({'success': True})


@csrf_exempt
def project_member_delete(request, project_id):
    if request.method == 'POST':
        user_id = request.POST.get('user_id', None)
        project = Project.objects.get(id=project_id)
        user = User.objects.get(id=user_id)
        project.members.remove(user)
        return JsonResponse({'success': True})

