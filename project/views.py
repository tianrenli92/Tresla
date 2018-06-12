from django.shortcuts import render

# Create your views here.


def project_list(request):

    return render(request, 'project/project_list.html', {})


def project_detail(request, project_id):

    return render(request, 'project/project_detail.html', {'project_id':project_id})
