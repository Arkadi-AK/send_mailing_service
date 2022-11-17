# -*- coding: utf-8 -*-


def send_message_to_email(clients, text):
    """
    The logic of sending a message to the mail
    """
    for item in clients:
        prepare_text = prepare_text_message(item, text)
        print("The message {text} has been sent to {name}".format(text=prepare_text, name=item['email']))
    return "OK"


def prepare_text_message(item, text):
    for i in item:
        text = text.replace("{" + i + "}", item[i].encode('utf8'))
    return text.encode('utf8')
