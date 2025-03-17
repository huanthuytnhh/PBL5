from django.contrib import admin
from django.urls import include, path

urlpatterns = [
    path("admin/", admin.site.urls),
    path("devices/", include("devices.urls")),  # Thêm "devices/" vào đây
    path("api/", include("api.urls")),
]
