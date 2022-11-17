# -*- coding: utf-8 -*-

from __future__ import absolute_import
from mailing.celery import app
from mailing_sender.email_sender import send_message_to_email


@app.task
def send_message_task(**kwargs):
    queryset = kwargs['queryset']
    text = kwargs['text']
    send_message_to_email(queryset, text)
