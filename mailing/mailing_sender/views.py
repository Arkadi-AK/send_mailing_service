# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.shortcuts import render, redirect

from mailing_sender.forms import MessageSendForm


def send_messages_view(request):
    if request.method == 'POST':
        form = MessageSendForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect('send_messages_view')
    else:
        form = MessageSendForm()
    return render(request, 'index.html', {"form": form})
