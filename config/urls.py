from django.conf import settings
from django.conf.urls.static import static
from django.contrib import admin
from django.urls import include, path

urlpatterns = [
    path("admin/", admin.site.urls),
    path("api/", include("catalog.urls")),
    path("api/", include("orders.urls")),
]

# No object storage (S3/Cloudinary) configured — serve uploaded media directly via Django.
urlpatterns += static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)
