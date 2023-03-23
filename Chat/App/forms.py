from django import forms
from .models import *
from django.contrib.auth.models import User


class EditAccountForm(forms.ModelForm):
    class Meta:
        model = User
        fields = ('username',)


class AccountForm(forms.ModelForm):
    class Meta:
        model = account
        fields = ('avatar',)

class ChatRoomForm(forms.ModelForm):
    class Meta:
        model = chatroom
        fields = ('__all__')
        