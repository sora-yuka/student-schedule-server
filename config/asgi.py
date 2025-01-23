"""
ASGI config for config project.

It exposes the ASGI callable as a module-level variable named ``application``.

For more information on this file, see
https://docs.djangoproject.com/en/5.1/howto/deployment/asgi/
"""

import os
import django

os.environ.setdefault('DJANGO_SETTINGS_MODULE', 'config.settings')
django.setup()

from django.core.asgi import get_asgi_application
from channels.auth import AuthMiddlewareStack
from channels.routing import ProtocolTypeRouter, URLRouter
from apps.chat.routing import websocket_urlpatterns
from apps.chat.middleware import JWTWebsocketMiddleware


application = ProtocolTypeRouter({
    "http": get_asgi_application(),
    "websocket": JWTWebsocketMiddleware(
        AuthMiddlewareStack(URLRouter(websocket_urlpatterns))
    )
})