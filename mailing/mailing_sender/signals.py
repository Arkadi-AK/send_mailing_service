# -*- coding: utf-8 -*-
from django.db.models.signals import post_save
from django.dispatch import receiver

from mailing_sender.models import Sender, Message, Client


@receiver(post_save, sender=Sender)
def post_save_sender(created, **kwargs):
    instance = kwargs['instance']
    clients = Client.objects.all()
    if created:
        for client in clients:
            Message(status="Отправлено", mailing=instance, client=client).save()
