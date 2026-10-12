from rest_framework import viewsets

from .models import Listing
from .serializers import ListingSerializer


class ListingViewSet(viewsets.ReadOnlyModelViewSet):
    queryset = Listing.objects.prefetch_related("images", "videos").all()
    serializer_class = ListingSerializer

    def get_queryset(self):
        queryset = super().get_queryset()
        category = self.request.query_params.get("category")
        if category:
            queryset = queryset.filter(category=category)
        return queryset
