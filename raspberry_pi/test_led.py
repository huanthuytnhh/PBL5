import sys
import time

from gpiozero import LED


def test_led(pin):
    """Test LED trên chân GPIO cụ thể"""
    try:
        led = LED(pin)
        print(f"Đang test LED trên chân GPIO {pin}")

        # Nhấp nháy LED 5 lần
        for i in range(5):
            led.on()
            print("LED bật")
            time.sleep(0.5)
            led.off()
            print("LED tắt")
            time.sleep(0.5)

        return True
    except Exception as e:
        print(f"Lỗi khi test LED trên chân GPIO {pin}: {e}")
        return False


def test_all_leds():
    """Test tất cả các LED đã cấu hình"""
    from control.config import LED_PINS

    print("Đang test tất cả các LED...")
    for name, pin in LED_PINS.items():
        print(f"\nTest LED {name} trên chân GPIO {pin}")
        if test_led(pin):
            print(f"LED {name} hoạt động tốt!")
        else:
            print(f"LED {name} không hoạt động!")


if __name__ == "__main__":
    if len(sys.argv) > 1:
        # Test LED cụ thể
        pin = int(sys.argv[1])
        test_led(pin)
    else:
        # Test tất cả LED
        test_all_leds()
