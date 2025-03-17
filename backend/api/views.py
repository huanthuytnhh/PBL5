from rest_framework.response import Response
from rest_framework.decorators import api_view
from .models import Device

@api_view(['GET', 'POST'])
def control_device(request):
    if request.method == 'POST':
        device_name = request.data.get('device')
        action = request.data.get('action')

        # Xử lý điều khiển thiết bị
        device = Device.objects.get(name=device_name)
        device.status = (action == "on")
        device.save()
        return Response({"message": f"{device_name} đã {action}"})

    return Response({"error": "Invalid request"})
