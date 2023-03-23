from django.urls import path, include
from .views import *
from rest_framework import routers

router = routers.DefaultRouter()
router.register(r'rooms', RoomList)

urlpatterns = [
    path('api/v1/', include(router.urls)),
    # path('accounts/signup', signUp, name='signup'),
    path('', Index, name='index'),
    # path('api/v1/rooms/<int:pk>', RoomApiView.as_view()),
    path('profile/', UserChange, name='profile'),
    path('create_room/', CreateRoom, name='create_room'),
    path('chat_rooms/', chat_rooms, name='chat_rooms'),
    path('chat_room/<int:pk>/', chat_room, name='chat_room'),
    path('edit_room/<int:pk>/', room_edit_delete, name='edit_room'),
    path('join_to_room/<int:pk>/', JoinToRoom, name='JoinToRoom'),
    path('out_from_room/<int:pk>/', OutFromRoom, name='OutFromRoom'),
    path('stats/', stats, name='stats'),
]
