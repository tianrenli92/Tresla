from rest_framework import viewsets
from .serializers import User, UserSerializer, Project, ProjectSerializer, ProjectMember, ProjectMemberSerializer, \
    TaskList, TaskListSerializer, Task, TaskSerializer,IssueSerializer,CommentSerializer,IssueAssigneeSerializer,Issue,Comment,IssueAssignee


class UserViewSet(viewsets.ModelViewSet):
    queryset = User.objects.all()
    serializer_class = UserSerializer


class ProjectViewSet(viewsets.ModelViewSet):
    queryset = Project.objects.all()
    serializer_class = ProjectSerializer


class ProjectMemberViewSet(viewsets.ModelViewSet):
    queryset = ProjectMember.objects.all()
    serializer_class = ProjectMemberSerializer


class TaskListViewSet(viewsets.ModelViewSet):
    queryset = TaskList.objects.all()
    serializer_class = TaskListSerializer


class TaskViewSet(viewsets.ModelViewSet):
    queryset = Task.objects.all()
    serializer_class = TaskSerializer

class IssueViewSet(viewsets.ModelViewSet):
    queryset = Issue.objects.all()
    serializer_class = IssueSerializer

class CommentViewSet(viewsets.ModelViewSet):
    queryset = Comment.objects.all()
    serializer_class = CommentSerializer

class IssueAssigneeViewSet(viewsets.ModelViewSet):
    queryset = IssueAssignee.objects.all()
    serializer_class = IssueAssigneeSerializer

