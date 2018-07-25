from django.contrib.auth.models import User
from django.http.response import JsonResponse, HttpResponse
from django.shortcuts import render, redirect
from django.views.decorators.csrf import csrf_exempt
from rest_framework.parsers import JSONParser
from .models import Message
from project.models import Project
from .serializers import MessageSerializer, UserSerializer


def index(request, project_id):
    if not request.user.is_authenticated:
        return redirect('login')
    if request.method == "GET":
        project = Project.objects.get(id=project_id)
        return render(request, 'communication_channel/channel_index.html',
                      {'users': User.objects.exclude(username=request.user.username),
                       'project': project,
                       })


def message_view(request, project_id, target_id):
    if request.method == "GET":
        project = Project.objects.get(id=project_id)
        user_id = request.user.id
        return render(request, "communication_channel/messages.html",
                      {'users': User.objects.exclude(username=request.user.username),
                       'target': User.objects.get(id=target_id),
                       'messages': Message.objects.filter(sender_id=user_id, receiver_id=target_id) |
                                   Message.objects.filter(sender_id=target_id, receiver_id=user_id),
                       'project': project})


@csrf_exempt
def user_list(request, user_id=None):
    """
    List all required messages, or create a new message.
    """
    if request.method == 'GET':
        if user_id:
            users = User.objects.filter(id=user_id)
        else:
            users = User.objects.all()
        serializer = UserSerializer(users, many=True, context={'request': request})
        return JsonResponse(serializer.data, safe=False)

    elif request.method == 'POST':
        data = JSONParser().parse(request)
        serializer = UserSerializer(data=data)
        if serializer.is_valid():
            serializer.save()
            return JsonResponse(serializer.data, status=201)
        return JsonResponse(serializer.errors, status=400)


@csrf_exempt
def message_list(request, project_id):
    """
    List all required messages, or create a new message.
    """
    if request.method == 'GET':
        sender_id = request.GET.get('sender_id', None)
        receiver_id = request.user.id

        messages = Message.objects.filter(sender_id=sender_id, receiver_id=receiver_id, is_read=False)
        serializer = MessageSerializer(messages, many=True, context={'request': request})
        for message in messages:
            message.is_read = True
            message.save()
        return JsonResponse(serializer.data, safe=False)

    elif request.method == 'POST':
        data = JSONParser().parse(request)
        serializer = MessageSerializer(data=data)
        if serializer.is_valid():
            serializer.save()
            return JsonResponse(serializer.data, status=201)
        return JsonResponse(serializer.errors, status=400)
