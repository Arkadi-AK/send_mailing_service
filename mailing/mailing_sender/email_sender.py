# -*- coding: utf-8 -*-
import time


def send_message_to_email(clients, text):
    """
    The logic of sending a message to the mail
    """
    for item in clients:
        print("The message {text} has been sent to {name}".format(text=text, name=item['email']))
    return "OK"


def prepare_text_message(text):
    text = ""
    message = ""
    return message
