"""
ASGI config for config project.

It exposes the ASGI callable as a module-level variable named ``application``.

For more information on this file, see
https://docs.djangoproject.com/en/4.1/howto/deployment/asgi/
"""

import os

from channels.routing import ProtocolTypeRouter, URLRouter
from django.contrib.staticfiles.handlers import ASGIStaticFilesHandler
from django.core.asgi import get_asgi_application

from websockets.v1.chats.urls import websocket_urlpatterns2

os.environ.setdefault("DJANGO_SETTINGS_MODULE", "config.settings")

django_asgi_app = ASGIStaticFilesHandler(get_asgi_application())

application = ProtocolTypeRouter(
    {
        "http": django_asgi_app,
        "websocket": URLRouter(websocket_urlpatterns2),
    }
)
