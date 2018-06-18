from django.shortcuts import render, get_object_or_404, redirect
from .models import Issue, Project
from django.core.paginator import Paginator, EmptyPage, PageNotAnInteger
from .forms import CommentForm, IssueForm,NewIssueForm
from django.http import Http404,HttpResponseRedirect
from django.shortcuts import render_to_response



def list_of_issue_by_project(request,project_id):
    projects = Project.objects.all()
    issue = Issue.objects.filter(status='published')
    template = 'project:issue_tracker/project/list_of_issue_by_project.html'
    context = {'projects': projects, 'issue': issue, 'project_id': project_id}
    return render(request, template, context)


def list_of_issue(request,project_id):
    issue = Issue.objects.filter(status='published')
    paginator = Paginator(issue, 10)
    page = request.GET.get('page')
    try:
        issues = paginator.page(page)
    except PageNotAnInteger:
        issues = paginator.page(1)
    except EmptyPage:
        issues = paginator.page(paginator.num_pages)
    template = 'issue_tracker/issue/list_of_issue.html'
    return render(request, template, {'issues': issues, 'page': page,'project_id':project_id})


def issue_detail(request, issue_id, project_id):
    issue = get_object_or_404(Issue,id=issue_id)
    context = {'issue': issue,'issue_id':issue_id,'project_id':project_id}
    if issue.status == 'published':
        template = 'issue_tracker/issue/issue_detail.html'
    else:
        template = 'issue_tracker/issue/issue_preview.html'
    return render(request, template, context)


def add_comment(request, issue_id, project_id):
    issue = get_object_or_404(Issue, id=issue_id)
    if request.method == 'POST':
        form = CommentForm(request.POST)
        if form.is_valid():
            comment = form.save(commit=False)
            comment.issue = issue
            comment.save()
            return redirect('project:issue_tracker:issue_detail', project_id=project_id, issue_id=issue.id)
    else:
        form = CommentForm()
    template = 'issue_tracker/issue/add_comment.html'
    context = {'form': form,'project_id':project_id}
    return render(request, template, context)


def new_issue(request, project_id):
    if request.method == 'POST':
        form = IssueForm(request.POST)
        if form.is_valid():
            issue = form.save(commit=False)
            issue.author = request.user
            issue.save()
            return redirect('project:issue_tracker:issue_detail',project_id=project_id,issue_id=issue.id)
    else:
        form = IssueForm()
    template = 'issue_tracker/issue/new_issue.html'
    context = {'form': form,'project_id':project_id}
    return render(request, template, context)

def edit_issue(request, project_id,issue_id):
    issue = get_object_or_404(Issue, id=issue_id)
    if request.method == 'POST':
        form = NewIssueForm(request.POST,instance=issue)
        if form.is_valid():
            issue = form.save(commit=False)
            issue.author = request.user
            issue.save()
            return redirect('project:issue_tracker:issue_detail',project_id=project_id,issue_id=issue_id)
    else:
        form = NewIssueForm(instance=issue)
    template = 'issue_tracker/issue/edit_issue.html'
    context = {'form': form,'project_id':project_id}
    return render(request, template, context)



def delete_issue(request,project_id,issue_id):
    if not request.user.is_staff or not request.user.is_superuser:
        raise Http404
    issue = get_object_or_404(Issue,id=issue_id)
    issue.delete()
    return redirect('project:issue_tracker:success_deletion',project_id=project_id,issue_id=issue_id)




