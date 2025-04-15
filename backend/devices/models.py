from django.db import models

class Device(models.Model):
    DEVICE_TYPES = [
        ('led', 'LED'),
        ('switch', 'Switch'),
        ('sensor', 'Sensor'),
        ('other', 'Other'),
    ]
    
    name = models.CharField(max_length=100)
    device_type = models.CharField(max_length=10, choices=DEVICE_TYPES, default='led')
    is_on = models.BooleanField(default=False)
    gpio_pin = models.IntegerField(null=True, blank=True)  # Cho Raspberry Pi
    ip_address = models.GenericIPAddressField(null=True, blank=True)  # Cho ESP32

    def __str__(self):
        return self.name
