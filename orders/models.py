from django.db import models

from catalog.models import Listing


class Order(models.Model):
    listing = models.ForeignKey(
        Listing, related_name="orders", on_delete=models.SET_NULL, null=True
    )
    full_name = models.CharField(max_length=255)
    phone = models.CharField(max_length=32)
    address_or_viewing_location = models.CharField(max_length=255)
    quantity = models.PositiveIntegerField(null=True, blank=True)
    preferred_date_time = models.DateTimeField(null=True, blank=True)
    notes = models.TextField(blank=True)
    created_at = models.DateTimeField(auto_now_add=True)

    class Meta:
        ordering = ["-created_at"]

    def __str__(self) -> str:
        listing_title = self.listing.title if self.listing else "(deleted listing)"
        return f"Order: {self.full_name} — {listing_title}"
