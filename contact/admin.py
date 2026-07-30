from django.contrib import admin
from .models import ContactMessage


@admin.register(ContactMessage)
class ContactMessageAdmin(admin.ModelAdmin):
    list_display = ["name", "email", "phone", "is_reviewed", "created_at"]
    list_filter = ["is_reviewed"]
    search_fields = ["name", "email", "message"]