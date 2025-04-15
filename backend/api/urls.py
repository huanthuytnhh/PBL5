from django.urls import path, include
from rest_framework.routers import DefaultRouter
from .views import DeviceViewSet

# Khởi tạo router cho REST framework
router = DefaultRouter()
router.register(r'devices', DeviceViewSet)

urlpatterns = [
    # Đưa các routes tự động được tạo bởi router vào urlpatterns
    path('', include(router.urls)),
]
