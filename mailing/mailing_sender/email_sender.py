# -*- coding: utf-8 -*-
from django.core.mail import send_mail


def send_message_to_email(clients, text):
    """
    The logic of sending a message to the mail
    """
    for item in clients:
        prepare_text = prepare_text_message(item, text)
        send_mail('subject_info', prepare_text, 'ARKADI-AK@yandex.ru',
                  [item['email']], fail_silently=False)
        print("The message {text} has been sent to {name}".format(text=prepare_text.encode('utf8'), name=item['email']))
    return "OK"


def prepare_text_message(item, text):
    for i in item:
        text = text.replace("{" + i + "}", item[i])
    return text
