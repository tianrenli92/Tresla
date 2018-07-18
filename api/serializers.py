from rest_framework import serializers
from django.contrib.auth.models import User
from project.models import Project, ProjectMember
from task_tracker.models import TaskList, Task
from issue_tracker.models import Issue,Comment,IssueAssignee


class UserSerializer(serializers.HyperlinkedModelSerializer):
    class Meta:
        model = User
        fields = ('url', 'username', 'email', 'is_staff')


class ProjectSerializer(serializers.HyperlinkedModelSerializer):
    class Meta:
        model = Project
        exclude=()


class ProjectMemberSerializer(serializers.HyperlinkedModelSerializer):
    class Meta:
        model = ProjectMember
        exclude=()

class TaskListSerializer(serializers.HyperlinkedModelSerializer):
    class Meta:
        model = TaskList
        exclude=()

class TaskSerializer(serializers.HyperlinkedModelSerializer):
    class Meta:
        model = Task
        exclude=()

class IssueSerializer(serializers.HyperlinkedModelSerializer):
    class Meta:
        model = Issue
        exclude=()

class CommentSerializer(serializers.HyperlinkedModelSerializer):
    class Meta:
        model = Comment
        exclude=()

class IssueAssigneeSerializer(serializers.HyperlinkedModelSerializer):
    class Meta:
        model = IssueAssignee
        exclude=()