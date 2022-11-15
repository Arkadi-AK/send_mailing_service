# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models


class Client(models.Model):
    first_name = models.CharField(max_length=50, null=False, verbose_name='Имя')
    last_name = models.CharField(max_length=50, null=False, verbose_name='Фамилия')
    birthday = models.DateTimeField(null=False, verbose_name='Время запуска рассылки')

    def __str__(self):
        return "Клиент" + str(self.last_name)

    class Meta:
        ordering = ['id']
        verbose_name = 'Клиент'
        verbose_name_plural = 'Клиенты'
