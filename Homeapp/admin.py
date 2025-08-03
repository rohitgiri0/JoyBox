from django.contrib import admin
from .models import ConsoleListing,Message, ChatRoom
# Register your models here.

@admin.register(ConsoleListing)
class ConsoleListingAdmin(admin.ModelAdmin):
    list_display = ['console_name', 'user', 'price', 'location', 'available', 'posted_at']
    search_fields = ['console_name', 'location']
    list_filter = ['available', 'location']


@admin.register(Message)
class MessageAdmin(admin.ModelAdmin):
    list_display = ('id', 'chat_room', 'sender', 'content', 'timestamp', 'is_read')
    list_filter = ('chat_room', 'sender', 'is_read')
    search_fields = ('content', 'sender__username', 'chat_room__id')
    ordering = ('-timestamp',)
    readonly_fields = ('timestamp',)

@admin.register(ChatRoom)
class ChatRoomAdmin(admin.ModelAdmin):
    list_display = ('id', 'user1', 'user2', 'created_at')
    search_fields = ('user1__username', 'user2__username')
    ordering = ('-created_at',)