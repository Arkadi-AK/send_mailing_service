# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.contrib import admin

from .models import Client, Sender, Message


class ClientAdmin(admin.ModelAdmin):
    list_display = ('id', 'first_name', 'last_name')
    list_display_links = ('id', 'first_name')
    save_on_top = True


class SenderAdmin(admin.ModelAdmin):
    list_display = ('id', 'start_mailing', 'stop_mailing', 'text')
    list_display_links = ('id',)


class MessageAdmin(admin.ModelAdmin):
    list_display = ('id', 'created_at', 'status', 'mailing', 'client')
    list_display_links = ('id',)
    list_filter = ('status',)
    save_on_top = True


admin.site.register(Sender, SenderAdmin)
admin.site.register(Client, ClientAdmin)
admin.site.register(Message, MessageAdmin)
