from django.shortcuts import render,get_list_or_404
from .models import Project
# Create your views here.


def project_index(request):
    project_list=get_list_or_404(Project,)
    return render(request, 'project/project_index.html', {'project_list':project_list})


def project_detail(request, project_id):

    return render(request, 'project/project_detail.html', {'project_id':project_id})

