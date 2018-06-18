from django.shortcuts import render,redirect
from django.utils.safestring import mark_safe
import json


def channel_index(request,project_id):
    if not request.user.is_authenticated:
        return redirect('login')
    if request.method == 'POST':
        return redirect('project:communication_channel:channel_view',project_id=project_id,channel_id=request.POST.get('channel_id'))
    if request.method == 'GET':
        return render(request, 'communication_channel/channel_index.html',
                      {'project_id': project_id,}
                      )


def channel_view(request, project_id, channel_id):
    return render(request, 'communication_channel/channel_view.html', {
        'channel_id_json': mark_safe(json.dumps(channel_id)),
        'project_id': project_id,
    })