# -*- coding: utf-8 -*-
from __future__ import unicode_literals
from django.utils.encoding import smart_unicode
from django.db import models

from tasks import send_message_task


class Client(models.Model):
    first_name = models.CharField(max_length=50, null=False, verbose_name='Имя')
    last_name = models.CharField(max_length=50, null=False, verbose_name='Фамилия')
    email = models.EmailField(verbose_name='e-mail')
    birthday = models.DateField(null=False, verbose_name='День рождения')

    def __unicode__(self):
        return smart_unicode(self.last_name)

    def __str__(self):
        return self.last_name

    class Meta:
        ordering = ['id']
        verbose_name = 'Клиент'
        verbose_name_plural = 'Клиенты'


class Sender(models.Model):
    start_mailing = models.DateTimeField(null=False, verbose_name='Время запуска рассылки')
    stop_mailing = models.DateTimeField(null=False, verbose_name='Время окончания рассылки')
    text = models.TextField(blank=True)

    def __str__(self):
        return "Рассылка {id}".format(id=self.id).encode('utf8')

    def save(self, *args, **kwargs):
        text = self.text
        eta = self.start_mailing
        expires = self.stop_mailing
        queryset = Client.objects.all().values('first_name', 'last_name', 'email', 'birthday')
        # queryset = Client.objects.all()
        queryset = list(queryset)
        super(Sender, self).save(*args, **kwargs)
        kw = {'queryset': queryset, 'text': text}
        send_message_task.apply_async(eta=eta, expires=expires, kwargs=kw)

    class Meta:
        ordering = ['id']
        verbose_name = 'Рассылка'
        verbose_name_plural = 'Рассылки'


class Message(models.Model):
    created_at = models.DateTimeField(auto_now=True, verbose_name='Дата создания')
    status = models.CharField(max_length=50, null=True, verbose_name='Статус отправки')
    mailing = models.ForeignKey(Sender, on_delete=models.CASCADE)
    client = models.ForeignKey(Client, on_delete=models.CASCADE)

    def __str__(self):
        return "Сообщение {id}".format(id=self.id).encode('utf8')

    class Meta:
        ordering = ['id']
        verbose_name = 'Сообщение'
        verbose_name_plural = 'Сообщения'
