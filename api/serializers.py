from rest_framework import serializers
from django.contrib.auth.models import User
from project.models import Project, ProjectMember
from task_tracker.models import TaskList, Task


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
