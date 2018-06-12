from django.contrib.auth.models import User  # Django Build in User Model
from django.http.response import JsonResponse
from django.views.decorators.csrf import csrf_exempt
from rest_framework.parsers import JSONParser
from .models import Message
from .serializers import MessageSerializer, UserSerializer  # Our Serializer Classes
from django.shortcuts import render,redirect


def channel_list(request, project_id):

    return render(request, 'communication_channel/channel_list.html', {'project_id': project_id})

<<<<<<< HEAD
from django.contrib.auth import authenticate, login #Django's inbuilt authentication methods
from django.shortcuts import render, redirect
<<<<<<< HEAD
=======
>>>>>>> 6709944bde6a76bb5f0e1917059e69c4b1e08110
=======
from chat.models import Message
from chat.serializers import MessageSerializer, UserSerializer
>>>>>>> parent of 74c02b5... html change

def channel_view(request):
    """Render the template with required context variables"""
    if not request.user.is_authenticated:
        return redirect('login')
    if request.method == "GET":
        return render(request, 'commuication_channel/templates/communication_channel/communication_channel.html',
                      {'users': User.objects.exclude(username=request.user.username)}) #Returning context for all users except the current logged-in user


# Users View
@csrf_exempt  # Decorator to make the view csrf excempt.
def user_list(request, pk=None):
    """
    List all required messages, or create a new message.
    """
    if request.method == 'GET':
        if pk:  # If PrimaryKey (id) of the user is specified in the url
            users = User.objects.filter(id=pk)  # Select only that particular user
        else:
            users = User.objects.all()  # Else get all user list
        serializer = UserSerializer(users, many=True, context={'request': request})
        return JsonResponse(serializer.data, safe=False)  # Return serialized data
    elif request.method == 'POST':
        data = JSONParser().parse(request)  # On POST, parse the request object to obtain the data in json
        serializer = UserSerializer(data=data)  # Seraialize the data
        if serializer.is_valid():
            serializer.save()  # Save it if valid
            return JsonResponse(serializer.data, status=201)  # Return back the data on success
        return JsonResponse(serializer.errors, status=400)  # Return back the errors  if not valid


@csrf_exempt
def message_list(request, sender=None, receiver=None):
    """
    List all required messages, or create a new message.
    """
    if request.method == 'GET':
        messages = Message.objects.filter(sender_id=sender, receiver_id=receiver)
        serializer = MessageSerializer(messages, many=True, context={'request': request})
        return JsonResponse(serializer.data, safe=False)
    elif request.method == 'POST':
        data = JSONParser().parse(request)
        serializer = MessageSerializer(data=data)
        if serializer.is_valid():
            serializer.save()
            return JsonResponse(serializer.data, status=201)
        return JsonResponse(serializer.errors, status=400)
