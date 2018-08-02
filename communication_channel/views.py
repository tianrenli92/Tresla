from django.contrib.auth.models import User
from django.http.response import JsonResponse, HttpResponse
from django.shortcuts import render, redirect
from django.views.decorators.csrf import csrf_exempt
from rest_framework.parsers import JSONParser
from .models import Message, ChannelMessage, Channel, ChannelForm
from project.models import Project
from .serializers import MessageSerializer, ChannelMessageSerializer
from django.utils.timezone import now


def channel_index(request, project_id):
    if not request.user.is_authenticated:
        return redirect('login')
    if request.method == "GET":
        project = Project.objects.get(id=project_id)
        channels = Channel.objects.filter(project_id=project_id)
        users = list(project.members.all()) + [project.owner]
        return render(request, 'communication_channel/channel_index.html',
                      {
                          'project': project,
                          'channels': channels,
                          'users': users,
                      })


def channel_create(request, project_id):
    if request.method == 'POST':
        channel = Channel(project_id=project_id)
        form = ChannelForm(request.POST, instance=channel)
        if form.is_valid():
            form.save()
        return redirect('project:communication_channel:channel_index', project_id=project_id)

    else:
        form = ChannelForm()
        return render(request, 'communication_channel/channel_create.html', {'form': form})


def channel_view(request, project_id, channel_id):
    if request.method == "GET":
        project = Project.objects.get(id=project_id)
        channels = Channel.objects.filter(project_id=project_id)
        channel = Channel.objects.get(id=channel_id)
        users = list(project.members.all()) + [project.owner]
        messages = ChannelMessage.objects.filter(channel_id=channel_id)
        if messages:
            latest_message_id = messages.latest('id').id
        else:
            latest_message_id = 0
        return render(request, "communication_channel/channel_view.html",
                      {'project': project,
                       'channels': channels,
                       'channel': channel,
                       'users': users,
                       'messages': messages,
                       'latest_message_id': latest_message_id,
                       })


@csrf_exempt
def channel_message_list(request, project_id, channel_id):
    """
    List all required messages, or create a new message.
    """
    if request.method == 'GET':
        latest_message_id = request.GET.get('latest_message_id', None)
        messages = ChannelMessage.objects.filter(channel_id=channel_id, id__gt=latest_message_id)
        serializer = ChannelMessageSerializer(messages, many=True, context={'request': request})
        data=serializer.data
        if messages:
            latest_message_id = messages.latest('id').id
            data=[{'latest_message_id':latest_message_id}]+data
        return JsonResponse(data, safe=False)

    elif request.method == 'POST':
        data = JSONParser().parse(request)
        serializer = ChannelMessageSerializer(data=data)
        if serializer.is_valid():
            serializer.save()
            latest_message_id = ChannelMessage.objects.latest('id').id
            data = {'latest_message_id': latest_message_id}
            return JsonResponse(data, status=201)
        return JsonResponse(serializer.errors, status=400)


def message_view(request, project_id, target_id):
    if request.method == "GET":
        project = Project.objects.get(id=project_id)
        channels = Channel.objects.filter(project_id=project_id)
        users = list(project.members.all()) + [project.owner]
        user_id = request.user.id
        messages = Message.objects.filter(sender_id=user_id, receiver_id=target_id) | Message.objects.filter(
            sender_id=target_id, receiver_id=user_id)
        return render(request, "communication_channel/message_view.html",
                      {'project': project,
                       'channels': channels,
                       'users': users,
                       'target': User.objects.get(id=target_id),
                       'messages': messages,
                       })


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
