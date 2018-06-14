from django.shortcuts import render,get_list_or_404, redirect
from .models import Project, ProjectForm
from django.contrib.auth.models import User
# Create your views here.


def project_index(request):
    project_list=get_list_or_404(Project)
    return render(request, 'project/project_index.html', {'project_list':project_list})


def project_detail(request, project_id):

    return render(request, 'project/project_detail.html', {'project_id':project_id})

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
