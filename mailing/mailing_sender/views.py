# -*- coding: utf-8 -*-
from __future__ import unicode_literals

import os.path

from django.http import HttpResponse
from django.shortcuts import render, redirect
from django.views import View

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


class PixelView(View):

    def get(self, request, *args, **kwargs):
        script_dir = os.path.dirname(os.path.abspath(__file__))
        image_data = open(os.path.join(script_dir, 'static/img/open-tracking/pixel.png'), 'rb').read()
        client_id = kwargs.get('client')
        return HttpResponse(image_data, content_type="image/png")
