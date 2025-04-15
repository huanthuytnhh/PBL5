from rest_framework import viewsets, permissions
from devices.models import Device
from .serializers import DeviceSerializer

class DeviceViewSet(viewsets.ModelViewSet):
    """
    API endpoint that allows devices to be viewed or edited.
    """
    queryset = Device.objects.all().order_by('name')
    serializer_class = DeviceSerializer
    # You can add permission classes back later, e.g.:
    # permission_classes = [permissions.IsAuthenticated] # Or AllowAny for testing
    permission_classes = [permissions.AllowAny] # Allow anyone for now
