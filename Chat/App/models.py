from django.db import models
from django.contrib.auth.models import User

# Create your models here.

class account(models.Model):
    user = models.OneToOneField(User, on_delete=models.CASCADE)
    avatar = models.ImageField(default='user.png', upload_to='images')


class chatroom(models.Model):
    name = models.CharField(max_length=64)
    author = models.ForeignKey(User, on_delete=models.CASCADE)
    create_date = models.DateTimeField(auto_now_add=True)
   

class message(models.Model):
    text = models.TextField()
    author = models.ForeignKey(account, on_delete=models.CASCADE)
    created_date = models.DateTimeField(auto_now_add=True)
    room = models.ForeignKey('chatroom', on_delete=models.CASCADE)


class members(models.Model):
    member = models.ForeignKey(account, on_delete=models.CASCADE)
    room = models.ForeignKey('chatroom', on_delete=models.CASCADE)


    
