from django.contrib import admin
from .models import Certificate


@admin.register(Certificate)
class CertificateAdmin(admin.ModelAdmin):
    list_display = ["title", "user", "issued_date", "created_at"]
    search_fields = ["title", "user__uid", "user__name"]
    list_filter = ["issued_date"]