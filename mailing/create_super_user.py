import os

from django.contrib.auth.models import User
from django.core.wsgi import get_wsgi_application

import mailing
from mailing import settings

os.environ.setdefault('DJANGO_SETTINGS_MODULE', {settings})

application = get_wsgi_application()

users = User.objects.all()
if not users:
    User.objects.create_superuser(username="username", email="user@example.com", password="password", is_active=True, is_staff=True)