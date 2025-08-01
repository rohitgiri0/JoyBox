from django.contrib import admin
from .models import ConsoleListing
# Register your models here.

@admin.register(ConsoleListing)
class ConsoleListingAdmin(admin.ModelAdmin):
    list_display = ['console_name', 'user', 'price', 'location', 'available', 'posted_at']
    search_fields = ['console_name', 'location']
    list_filter = ['available', 'location']