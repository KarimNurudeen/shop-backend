from rest_framework import serializers

from .models import Order


class OrderSerializer(serializers.ModelSerializer):
    listing_id = serializers.CharField(write_only=True)

    class Meta:
        model = Order
        fields = [
            "id",
            "listing_id",
            "full_name",
            "phone",
            "address_or_viewing_location",
            "quantity",
            "preferred_date_time",
            "notes",
            "created_at",
        ]
        read_only_fields = ["id", "created_at"]
