"""
WSGI config for myAssistant project.

It exposes the WSGI callable as a module-level variable named ``application``.

For more information on this file, see
https://docs.djangoproject.com/en/4.2/howto/deployment/wsgi/
"""

import os
import sys

from django.core.wsgi import get_wsgi_application

path = "/home/keoinn/django_env/lib/python3.10/site-packages"
if path not in sys.path:
    sys.path.insert(0, path)
path = "/home/keoinn/myAssistant"
if path not in sys.path:
    sys.path.insert(0, path)

os.environ.setdefault('DJANGO_SETTINGS_MODULE', 'myAssistant.settings')

application = get_wsgi_application()
