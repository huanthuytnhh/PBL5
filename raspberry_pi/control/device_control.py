import os
import sys

import requests

sys.path.append(os.path.abspath(os.path.join(os.path.dirname(__file__), "..", "..")))
from raspberry_pi.control.led_config import API_URL

# Import API_URL từ config.py


def send_command(device, action):
    """Gửi lệnh điều khiển thiết bị đến backend Django"""
    data = {"device": device, "action": action}
    # response = requests.post("http://127.0.0.1:8000/api/control_device/", json=data)
    response = requests.post(
        "http://127.0.0.1:8000/api/devices/control_device/", json=data
    )

    if response.status_code == 200:
        return response.json()  # Trả về kết quả từ API
    else:
        return {"error": "Failed to send command"}


# Test thử
if __name__ == "__main__":
    print(send_command("light", "on"))
