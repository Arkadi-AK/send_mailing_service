# -*- coding: utf-8 -*-

from __future__ import absolute_import

from datetime import datetime

from django import forms
from django.forms import DateTimeInput

from mailing_sender.models import Sender


class MessageSendForm(forms.ModelForm):
    start_mailing = forms.DateTimeField(required=False,
                                        widget=DateTimeInput(attrs={'type': 'datetime-local'}),
                                        initial=format(datetime.now(), '%Y-%m-%dT%H:%M'),
                                        input_formats=['%Y-%m-%dT%H:%M'])
    stop_mailing = forms.DateTimeField(required=False,
                                       widget=DateTimeInput(attrs={'type': 'datetime-local'}),
                                       initial=format(datetime.now(), '%Y-%m-%dT%H:%M'),
                                       input_formats=['%Y-%m-%dT%H:%M'])

    class Meta:
        model = Sender
        fields = '__all__'
        widgets = {
            'start_mailing': forms.DateTimeInput(attrs={'type': 'datetime-local'}),
            'stop_mailing': forms.DateTimeInput(attrs={'type': 'datetime-local'}),
            'text': forms.Textarea(),
            # 'category': forms.Select(attrs={'class': 'form-control'}),
        }
