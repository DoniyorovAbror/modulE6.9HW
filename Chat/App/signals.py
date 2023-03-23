from django.db.models.signals import post_save
from django.contrib.auth.models import User
from .models import *
from django.conf import settings
from django.dispatch import receiver


@receiver(post_save, sender=User)
def create_account(sender, instance, created, **kwargs):
    if created:
        account.objects.create(user = instance)

@receiver(post_save, sender=User)
def save_account(sender, instance, **kwargs):
    if not instance.is_superuser:
        instance.account.save()


@receiver(post_save, sender=chatroom)
def save_room(sender, instance, **kwargs):
    _member = account.objects.get(id=instance.author.id)
    _room = chatroom.objects.get(id=instance.id)
    members.objects.create(member=_member, room=_room)
    

def createAccount(sender, **kwargs):
    if kwargs['created']:
        user_account = account.objects.create(user=kwargs['instance'])
        post_save.connect(createAccount, sender=User)