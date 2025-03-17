from django.http import JsonResponse


def get_devices(request):
    return JsonResponse({"message": "List of devices"})
