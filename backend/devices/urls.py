from django.urls import path

from .views import get_devices  # Kiểm tra xem đã import chưa

urlpatterns = [
    path("", get_devices, name="get_devices"),
]
