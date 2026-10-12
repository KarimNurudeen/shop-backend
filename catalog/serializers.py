from rest_framework import serializers

from .models import Listing, ListingImage, ListingVideo


class ListingImageSerializer(serializers.Serializer):
    def to_representation(self, instance: ListingImage) -> str:
        if instance.image:
            request = self.context.get("request")
            url = instance.image.url
            return request.build_absolute_uri(url) if request else url
        return instance.url


class ListingVideoSerializer(serializers.Serializer):
    def to_representation(self, instance: ListingVideo) -> str:
        return instance.video_url


class ListingSerializer(serializers.ModelSerializer):
    id = serializers.CharField(source="pk", read_only=True)
    images = ListingImageSerializer(many=True, read_only=True)
    videos = ListingVideoSerializer(many=True, read_only=True)

    class Meta:
        model = Listing
        fields = [
            "id",
            "category",
            "title",
            "price",
            "images",
            "videos",
            "location",
            "beds",
            "baths",
            "sqft",
            "brand",
            "rating",
            "review_count",
            "in_stock",
            "description",
            "seller_name",
        ]
