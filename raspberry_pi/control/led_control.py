from gpiozero import LED

from .device_control import send_command

# Định nghĩa chân GPIO cho các LED
GPIO_PINS = {
    "led": 17,  # LED mặc định
    "led_phong_khach": 18,  # LED phòng khách
    "led_phong_ba_me": 22,  # LED phòng ba mẹ
    "led_phong_con_trai": 23,  # LED phòng con trai
    "led_bep": 24,  # LED bếp
}


class RealLED:
    def __init__(self, name, pin):
        self.name = name
        self.led = LED(pin)

    def on(self):
        self.led.on()

    def off(self):
        self.led.off()

    def toggle(self):
        self.led.toggle()

    @property
    def is_lit(self):
        return self.led.is_lit


# Khởi tạo các đối tượng LED thật
leds = {}
for name, pin in GPIO_PINS.items():
    try:
        leds[name] = RealLED(name, pin)
        print(f"Đã khởi tạo LED {name} trên chân GPIO {pin}")
    except Exception as e:
        print(f"Lỗi khi khởi tạo LED {name} trên chân GPIO {pin}: {e}")


def turn_on_led(led_name="led"):
    """Bật LED"""
    if led_name in leds:
        led_obj = leds[led_name]
        led_obj.on()
        # Gửi trạng thái lên server
        result = send_command(led_name, "on")
        print(f"{led_name} status:", led_obj.is_lit)
        return f"Đã bật đèn {led_name}"
    return f"Không tìm thấy đèn {led_name}"


def turn_off_led(led_name="led"):
    """Tắt LED"""
    if led_name in leds:
        led_obj = leds[led_name]
        led_obj.off()
        # Gửi trạng thái lên server
        result = send_command(led_name, "off")
        print(f"{led_name} status:", led_obj.is_lit)
        return f"Đã tắt đèn {led_name}"
    return f"Không tìm thấy đèn {led_name}"


def toggle_led(led_name="led"):
    """Đảo trạng thái LED"""
    if led_name in leds:
        led_obj = leds[led_name]
        led_obj.toggle()
        state = "on" if led_obj.is_lit else "off"
        # Gửi trạng thái lên server
        result = send_command(led_name, state)
        print(f"{led_name} status:", led_obj.is_lit)
        return f"Đã chuyển đèn {led_name} sang trạng thái {state}"
    return f"Không tìm thấy đèn {led_name}"


# from .device_control import send_command


# class VirtualLED:
#     def __init__(self, name):
#         self.name = name
#         self.status = False

#     def on(self):
#         self.status = True

#     def off(self):
#         self.status = False

#     def toggle(self):
#         self.status = not self.status

#     @property
#     def is_lit(self):
#         return self.status


# # Khởi tạo các LED ảo
# led = VirtualLED("led")  # LED mặc định
# led_phong_khach = VirtualLED("led_phong_khach")
# led_phong_ba_me = VirtualLED("led_phong_ba_me")
# led_phong_con_trai = VirtualLED("led_phong_con_trai")
# led_bep = VirtualLED("led_bep")

# # Từ điển ánh xạ tên LED với đối tượng LED
# leds = {
#     "led": led,
#     "led_phong_khach": led_phong_khach,
#     "led_phong_ba_me": led_phong_ba_me,
#     "led_phong_con_trai": led_phong_con_trai,
#     "led_bep": led_bep,
# }


# def turn_on_led(led_name="led"):
#     """Bật LED"""
#     if led_name in leds:
#         led_obj = leds[led_name]
#         led_obj.on()
#         # Gửi trạng thái lên server
#         result = send_command(led_name, "on")
#         print(f"{led_name} status:", led_obj.is_lit)
#         return f"Đã bật đèn {led_name}"
#     return f"Không tìm thấy đèn {led_name}"


# def turn_off_led(led_name="led"):
#     """Tắt LED"""
#     if led_name in leds:
#         led_obj = leds[led_name]
#         led_obj.off()
#         # Gửi trạng thái lên server
#         result = send_command(led_name, "off")
#         print(f"{led_name} status:", led_obj.is_lit)
#         return f"Đã tắt đèn {led_name}"
#     return f"Không tìm thấy đèn {led_name}"


# def toggle_led(led_name="led"):
#     """Đảo trạng thái LED"""
#     if led_name in leds:
#         led_obj = leds[led_name]
#         led_obj.toggle()
#         state = "on" if led_obj.is_lit else "off"
#         # Gửi trạng thái lên server
#         result = send_command(led_name, state)
#         print(f"{led_name} status:", led_obj.is_lit)
#         return f"Đã chuyển đèn {led_name} sang trạng thái {state}"
#     return f"Không tìm thấy đèn {led_name}"
