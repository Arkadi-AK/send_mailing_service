# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.apps import AppConfig


class MailingSenderConfig(AppConfig):
    name = 'mailing_sender'

    def ready(self):
        import mailing_sender.signals
