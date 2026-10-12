from django.contrib import admin
from unfold.admin import ModelAdmin, TabularInline

from .models import Listing, ListingImage, ListingVideo


class ListingImageInline(TabularInline):
    model = ListingImage
    extra = 1
    fields = ["image", "url", "order"]


class ListingVideoInline(TabularInline):
    model = ListingVideo
    extra = 0
    fields = ["video_url", "order"]


@admin.register(Listing)
class ListingAdmin(ModelAdmin):
    list_display = ["title", "category", "price", "seller_name", "created_at"]
    list_filter = ["category"]
    search_fields = ["title", "seller_name", "location", "brand"]
    inlines = [ListingImageInline, ListingVideoInline]
