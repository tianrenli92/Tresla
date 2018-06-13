from django.contrib.auth.models import User  # Django Build in User Model
from django.http.response import JsonResponse
from django.views.decorators.csrf import csrf_exempt
from rest_framework.parsers import JSONParser
from .models import Message
from .serializers import MessageSerializer, UserSerializer  # Our Serializer Classes
from django.shortcuts import render,redirect


def channel_view(request,project_id):
    """Render the template with required context variables"""
    if not request.user.is_authenticated:
        return redirect('login')
    if request.method == "GET":
        return render(request, 'communication_channel/communication_view.html',
                      {'users': User.objects.exclude(username=request.user.username),
                       'project_id': project_id,
                       }
        ) #Returning context for all users except the current logged-in user

def message_view(request, sender, receiver):
    """Render the template with required context variables"""
    if not request.user.is_authenticated:
        return redirect('login')
    if request.method == "GET":
        return render(request, "communication_channel/messages.html",
                      {'users': User.objects.exclude(username=request.user.username), #List of users
                       'receiver': User.objects.get(id=receiver), # Receiver context user object for using in template
                       'messages': Message.objects.filter(sender_id=sender, receiver_id=receiver) |
                                   Message.objects.filter(sender_id=receiver, receiver_id=sender)}) # Return context with message objects where users are either sender or receiver.


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
