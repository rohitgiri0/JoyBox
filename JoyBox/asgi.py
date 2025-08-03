"""
ASGI config for JoyBox project.

It exposes the ASGI callable as a module-level variable named ``application``.

For more information on this file, see
https://docs.djangoproject.com/en/5.2/howto/deployment/asgi/
"""
import os
from django.core.asgi import get_asgi_application
from channels.auth import AuthMiddlewareStack
from channels.routing import ProtocolTypeRouter, URLRouter
import Homeapp.routing  # ✅ Make sure this matches your app folder

os.environ.setdefault('DJANGO_SETTINGS_MODULE', 'JoyBox.settings')

application = ProtocolTypeRouter({
    "http": get_asgi_application(),
    "websocket": AuthMiddlewareStack(
        URLRouter(
            Homeapp.routing.websocket_urlpatterns  # ✅ must point to your websocket_urlpatterns
        )
    ),
})