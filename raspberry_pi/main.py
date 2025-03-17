import signal
import sys

from voice.speech_recognition import process_command, recognize_speech


# Xử lý tín hiệu SIGTERM để tắt tất cả đèn khi thoát
def signal_handler(sig, frame):
    from control.led_control import turn_off_led

    print("\nĐang tắt tất cả đèn...")
    for led_name in [
        "led",
        "led_phong_khach",
        "led_phong_ba_me",
        "led_phong_con_trai",
        "led_bep",
    ]:
        turn_off_led(led_name)
    print("Đã tắt tất cả đèn")
    print("Đã dừng chương trình")
    sys.exit(0)


signal.signal(signal.SIGINT, signal_handler)
signal.signal(signal.SIGTERM, signal_handler)


def main():
    print("Chương trình điều khiển LED bằng giọng nói (Phiên bản Raspberry Pi)")
    print("Nói 'bật đèn', 'tắt đèn' hoặc 'chuyển đèn' để điều khiển")
    print("Nói 'bật đèn phòng khách', 'tắt đèn bếp', v.v. để điều khiển đèn cụ thể")
    print("Nói 'bật tất cả đèn' hoặc 'tắt hết đèn' để điều khiển tất cả đèn")
    print("Nhấn Ctrl+C để thoát")

    while True:
        try:
            # Nhận diện giọng nói
            text = recognize_speech()

            if text:
                # Xử lý lệnh
                result = process_command(text)
                print(result)

            # Hỏi người dùng có muốn tiếp tục không
            choice = input("Tiếp tục? (y/n): ")
            if choice.lower() != "y":
                # Tắt tất cả đèn khi thoát
                signal_handler(None, None)
                break

        except KeyboardInterrupt:
            # Tắt tất cả đèn khi thoát
            signal_handler(None, None)
            break


if __name__ == "__main__":
    main()
