from rest_framework import serializers
from devices.models import Device

class DeviceSerializer(serializers.HyperlinkedModelSerializer):
    class Meta:
        model = Device
        # Include 'url' for hyperlinked relations in DRF browsable API
        fields = ['url', 'id', 'name', 'device_type', 'is_on', 'gpio_pin', 'ip_address']
