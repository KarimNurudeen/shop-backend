from django.db import models


class Listing(models.Model):
    class Category(models.TextChoices):
        HOUSE = "house", "House"
        GADGET = "gadget", "Gadget"

    category = models.CharField(max_length=10, choices=Category.choices)
    title = models.CharField(max_length=255)
    price = models.DecimalField(max_digits=12, decimal_places=2)
    description = models.TextField()
    seller_name = models.CharField(max_length=255)

    # House-only fields
    location = models.CharField(max_length=255, blank=True)
    beds = models.PositiveIntegerField(null=True, blank=True)
    baths = models.PositiveIntegerField(null=True, blank=True)
    sqft = models.PositiveIntegerField(null=True, blank=True)

    # Gadget-only fields
    brand = models.CharField(max_length=255, blank=True)
    rating = models.DecimalField(max_digits=2, decimal_places=1, null=True, blank=True)
    review_count = models.PositiveIntegerField(null=True, blank=True)
    in_stock = models.BooleanField(null=True, blank=True)

    created_at = models.DateTimeField(auto_now_add=True)

    class Meta:
        ordering = ["-created_at"]

    def __str__(self) -> str:
        return self.title


class ListingImage(models.Model):
    listing = models.ForeignKey(Listing, related_name="images", on_delete=models.CASCADE)
    image = models.ImageField(upload_to="listings/images/", blank=True, null=True)
    url = models.URLField(blank=True)
    order = models.PositiveIntegerField(default=0)

    class Meta:
        ordering = ["order", "id"]

    def __str__(self) -> str:
        return f"{self.listing.title} image {self.order}"


class ListingVideo(models.Model):
    listing = models.ForeignKey(Listing, related_name="videos", on_delete=models.CASCADE)
    video_url = models.URLField()
    order = models.PositiveIntegerField(default=0)

    class Meta:
        ordering = ["order", "id"]

    def __str__(self) -> str:
        return f"{self.listing.title} video {self.order}"
