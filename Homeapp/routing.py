from django.urls import re_path
from . import consumers
print("✅ WebSocket routing loaded.")
websocket_urlpatterns = [
    re_path(r'ws/chat/(?P<room_id>\w+)/$', consumers.ChatConsumer.as_asgi()),
]