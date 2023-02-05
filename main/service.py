from django.conf import settings
from django.core.mail import send_mail
from django.template.loader import render_to_string


def send(name, last_name, birthday, list_mail, layout):
    msg = render_to_string('{}.html'.format(layout),
                           {'name': name, 'last_name': last_name, 'birthday': birthday, 'language': layout})
    send_mail('Hello {}, you have subscribed to the newsletter'.format(name),
              msg, settings.EMAIL_HOST_USER,
              list_mail,
              html_message=msg)
