from django.shortcuts import render, get_object_or_404, redirect
from .models import Issue, Project
from django.core.paginator import Paginator, EmptyPage, PageNotAnInteger
from .forms import CommentForm, IssueForm



def issue_list(request, project_id):

    return render(request, 'issue_tracker/issue_list.html', {'project_id': project_id})


def list_of_issue_by_project(request, project_slug):
    projects = Project.objects.all()
    issue = Issue.objects.filter(status='published')
    if project_slug:
        project = get_object_or_404(Project, slug=project_slug)
        issue = issue.filter(project=project)
    template = 'issue_tracker/project/list_of_issue_by_project.html'
    context = {'projects': projects, 'issue': issue, 'project': project}
    return render(request, template, context)


def list_of_issue(request):
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
    return render(request, template, {'issues': issues, 'page': page})


def issue_detail(request, slug):
    issue = get_object_or_404(Issue, slug=slug)
    context = {'issue': issue}
    if issue.status == 'published':
        template = 'issue_tracker/issue/issue_detail.html'
    else:
        template = 'issue_tracker/issue/issue_preview.html'
    return render(request, template, context)


def add_comment(request, slug):
    issue = get_object_or_404(Issue, slug=slug)
    if request.method == 'POST':
        form = CommentForm(request.POST)
        if form.is_valid():
            comment = form.save(commit=False)
            comment.issue = issue
            comment.save()
            return redirect('issue_tracker:issue_detail', slug=issue.slug)
    else:
        form = CommentForm()
    template = 'issue_tracker/issue/add_comment.html'
    context = {'form': form}
    return render(request, template, context)


def new_issue(request):
    if request.method == 'POST':
        form = IssueForm(request.POST)
        if form.is_valid():
            issue = form.save(commit=False)
            issue.author = request.user
            issue.save()
            return redirect('issue_tracker:issue_detail', slug=issue.slug)
    else:
        form = IssueForm()
    template = 'issue_tracker/issue/new_issue.html'
    context = {'form': form}
    return render(request, template, context)





