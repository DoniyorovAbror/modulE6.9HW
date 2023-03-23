from django.shortcuts import render, redirect
from .models import *
from django.contrib.auth.models import User
from rest_framework.views import APIView
from rest_framework.viewsets import ModelViewSet
from rest_framework.response import Response
from rest_framework.permissions import IsAuthenticatedOrReadOnly
from .serializers import RoomSerializer, UserSerializer
from django.views.generic import TemplateView, CreateView
from .forms import *
from django.contrib.auth.decorators import login_required
from django.conf import settings
# Create your views here.


class RoomList(ModelViewSet):
    queryset = chatroom.objects.all()
    serializer_class = RoomSerializer
    permission_class = (IsAuthenticatedOrReadOnly,)
        
    def post(self, request, format=None):
        
        content = {
            'user': str(request.user),
            'auth': str(request.auth),
        }
        return Response(content)
        
    
def UserChange(request):
    if request.method == 'POST':
        user_form = EditAccountForm(request.POST, instance=request.user)
        profile_form = AccountForm(request.POST, request.FILES, instance=request.user.account)

        if user_form.is_valid() and profile_form.is_valid():
            user_form = user_form.save()
            profile_form = profile_form.save(commit=False)
            profile_form.save()
            return redirect('/')
    else:
        user_form = EditAccountForm(instance=request.user)
        profile_form = AccountForm(instance=request.user.account)
        args = {}
        args['user_form'] = user_form
        args['profile_form'] = profile_form
        return render(request, template_name='account.html', context=args)


def Index(request):    
    return render(request, 'index.html')

@login_required
def CreateRoom(request):
    form = ChatRoomForm
    return render(request, 'create_room.html', context={'form':form})

@login_required
def room_edit_delete(request, pk):
    form = ChatRoomForm
    room_id = pk
    
    return render(request, template_name='edit_room.html', context={'form': form, 'room_id': room_id})

@login_required
def chat_room(request, pk):
    room = chatroom.objects.get(pk=pk)
    _members = members.objects.filter(room_id=pk)
    messages = message.objects.filter(room=room)
    username = []
    avatar = []
    
    for item in _members:
        username += User.objects.filter(id=item.member_id).values('username')
        avatar += account.objects.filter(user_id=item.member_id).values('avatar')

    _account = zip(username, avatar)
    media_url = settings.MEDIA_URL
    context = {
        'chat_room' : room,
        'members' : _account,
        'media' : media_url,
        'message' : messages,
    }
    return render(request, template_name='room.html', context=context)

def chat_rooms(request):
    rooms = chatroom.objects.all()
    _member = members.objects.filter(member_id=request.user.id).values_list('room_id', flat=True)
    return render(request, template_name='rooms.html', context={'contents':rooms, 'members': _member})

def JoinToRoom(request, *args, **kwargs):
    _member = account.objects.get(id=request.user.id)
    _room = chatroom.objects.get(id=kwargs['pk'])
    members.objects.create(room=_room, member=_member)
    return redirect(f'/chat_room/{kwargs["pk"]}/')

def OutFromRoom(request, *args, **kwargs):
    _member = account.objects.get(id=request.user.id)
    _room = chatroom.objects.get(id=kwargs['pk'])
    members.objects.filter(room=_room, member=_member).delete()

    return redirect('chat_rooms')

def stats(request):
    rooms = chatroom.objects.all().count()
    _members = members.objects.all().count()
    _messsages = message.objects.all().count()
    return render(request, template_name='statistics.html', context={'rooms': rooms, 'members': _members, 'messages': _messsages})