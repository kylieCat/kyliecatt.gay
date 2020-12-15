from django.conf import settings
from django.conf.urls.static import static
from django.contrib import admin
from django.urls import path, include

from .health_check import HealthCheckView


urlpatterns = [
    path('admin/', admin.site.urls),
    path("hc/", HealthCheckView.as_view(), name="health_check"),
    path("", include("ui.urls")),
    path("", include("redirects.urls")),
] + static(settings.STATIC_URL, document_root=settings.STATIC_ROOT)

