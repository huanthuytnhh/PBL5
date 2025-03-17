from django.urls import path

from .views import control_device

urlpatterns = [
    path("devices/control_device/", control_device, name="control_device"),
]
