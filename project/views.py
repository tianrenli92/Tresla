from django.shortcuts import render,get_list_or_404, redirect
from .models import Project, ProjectList, ProjectListForm
# Create your views here.


def project_index(request):
    project_list=get_list_or_404(Project)
    return render(request, 'project/project_index.html', {'project_list':project_list})


def project_detail(request, project_id):

    return render(request, 'project/project_detail.html', {'project_id':project_id})

def project_create(request):
    if request.method == 'POST':
        project_list = ProjectList
        form = ProjectListForm(request.POST,instance=project_list)
        if form.is_valid():
            form.save()
        return redirect('project:project_index')

    else:
        form=ProjectListForm()
        return render(request, 'project/project_creat.html', {'form':form})
