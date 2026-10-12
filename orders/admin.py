from django.contrib import admin
from unfold.admin import ModelAdmin

from .models import Order


@admin.register(Order)
class OrderAdmin(ModelAdmin):
    list_display = [
        "full_name",
        "phone",
        "listing",
        "quantity",
        "preferred_date_time",
        "created_at",
    ]
    list_filter = ["created_at"]
    search_fields = ["full_name", "phone", "address_or_viewing_location"]
    readonly_fields = [
        "listing",
        "full_name",
        "phone",
        "address_or_viewing_location",
        "quantity",
        "preferred_date_time",
        "notes",
        "created_at",
    ]

    def has_add_permission(self, request):
        return False
