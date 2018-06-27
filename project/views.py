from django.shortcuts import render,get_list_or_404, redirect, get_object_or_404
from .models import Project, ProjectForm,UserSerializer,User
from django.contrib.auth.models import User
from django.http import Http404,HttpResponse
from django.core import serializers
from .serializers import UserSerializers
from rest_framework import generics
from rest_framework.renderers import JSONRenderer
from rest_framework.parsers import JSONParser
from django.http import HttpResponse,JsonResponse
from django.views.decorators.csrf import csrf_exempt


def project_index(request):
    project_list=get_list_or_404(Project)
    return render(request, 'project/project_index.html', {'project_list':project_list})


def project_detail(request, project_id):
    users = User.objects.all()
    return render(request, 'project/project_detail.html', {'project_id':project_id,'users':users})


def project_create(request):
    if request.method == 'POST':
        project = Project(owner_id=request.user.id)
        form = ProjectForm(request.POST,instance=project)
        if form.is_valid():
            form.save()
        return redirect('project:project_index')

    else:
        form=ProjectForm()
        return render(request, 'project/project_create.html', {'form':form})


def project_delete(request, project_id):
    try:
        instance=Project.objects.get(id=project_id)
    except Project.DoesNotExist:
        raise Http404("No such project.")
    instance.delete()
    return redirect('project:delete_result',project_id=project_id)


def project_edit(request, project_id):
    project = get_object_or_404(Project, id=project_id)
    form = ProjectForm(request.POST or None, instance=project)
    if form.is_valid():
        form.save()
        return redirect('project:project_index')
    return render(request, 'project/project_edit.html', {'form': form})

@csrf_exempt
def add_member(request,project_id,user_id):
    project = get_object_or_404(Project, id=project_id)
    user = get_object_or_404(User, id=user_id)
    form = request.POST.get(User,None)
    if request.method=='POST':
        form = request.GET.get(User, None)
        if form.is_valid():
            form.save()
            return redirect('project:delete_index')
        else:
            form = User()

    return render(request,'project/project_add_member.html',{'form':form,'project_id':project_id,'user_id':user_id})
