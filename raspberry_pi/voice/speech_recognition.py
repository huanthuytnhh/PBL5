import datetime
import os
import sys

import speech_recognition as sr

sys.path.append(os.path.abspath(os.path.join(os.path.dirname(__file__), "..")))
from control.config import MIC_INDEX
from control.led_control import toggle_led, turn_off_led, turn_on_led

# Tạo thư mục logs nếu chưa tồn tại
LOG_DIR = os.path.join(os.path.dirname(os.path.dirname(__file__)), "logs")
os.makedirs(LOG_DIR, exist_ok=True)
LOG_FILE = os.path.join(LOG_DIR, "speech_log.txt")


def log_speech(text):
    """Ghi nội dung nhận diện vào file"""
    timestamp = datetime.datetime.now().strftime("%Y-%m-%d %H:%M:%S")
    with open(LOG_FILE, "a", encoding="utf-8") as file:
        file.write(f"[{timestamp}] {text}\n")


def recognize_speech():
    """Nhận diện giọng nói và trả về văn bản"""
    recognizer = sr.Recognizer()

    try:
        with sr.Microphone(device_index=MIC_INDEX) as source:
            print("Đang lắng nghe...")
            # Điều chỉnh độ nhạy của microphone
            recognizer.adjust_for_ambient_noise(source, duration=1)
            print("Bắt đầu nói...")
            try:
                # Tăng timeout lên 10 giây
                audio = recognizer.listen(source, timeout=10, phrase_time_limit=5)
                print("Đã ghi âm xong, đang xử lý...")
            except sr.WaitTimeoutError:
                print("Không phát hiện giọng nói trong thời gian chờ")
                log_speech("[Không phát hiện giọng nói]")
                return ""

        try:
            text = recognizer.recognize_google(audio, language="vi-VN")
            print(f"Đã nhận diện được: '{text}'")
            log_speech(text)
            return text.lower()
        except sr.UnknownValueError:
            print("Không thể nhận diện được giọng nói")
            log_speech("[Không thể nhận diện được giọng nói]")
            return ""
        except sr.RequestError as e:
            print(f"Lỗi khi gửi yêu cầu đến Google Speech Recognition: {e}")
            log_speech(f"[Lỗi Google Speech Recognition: {e}]")
            return ""
    except Exception as e:
        print(f"Lỗi khi sử dụng microphone: {e}")
        log_speech(f"[Lỗi microphone: {e}]")
        return ""


def process_command(text):
    """Xử lý lệnh giọng nói"""
    response = "Không hiểu lệnh"

    # Xác định phòng từ lệnh
    room = None
    if "phòng khách" in text:
        room = "led_phong_khach"
    elif "phòng ba mẹ" in text or "phòng bố mẹ" in text or "phòng ngủ" in text:
        room = "led_phong_ba_me"
    elif "phòng con" in text or "phòng con trai" in text:
        room = "led_phong_con_trai"
    elif "bếp" in text or "nhà bếp" in text:
        room = "led_bep"
    else:
        room = "led"  # Mặc định

    # Xử lý hành động
    if "bật đèn" in text or "mở đèn" in text:
        response = turn_on_led(room)
    elif "tắt đèn" in text:
        response = turn_off_led(room)
    elif "chuyển đèn" in text or "đảo đèn" in text:
        response = toggle_led(room)
    elif "tắt hết đèn" in text or "tắt tất cả đèn" in text:
        # Tắt tất cả đèn
        responses = []
        for led_name in [
            "led",
            "led_phong_khach",
            "led_phong_ba_me",
            "led_phong_con_trai",
            "led_bep",
        ]:
            responses.append(turn_off_led(led_name))
        response = "Đã tắt tất cả đèn"
    elif "bật hết đèn" in text or "bật tất cả đèn" in text:
        # Bật tất cả đèn
        responses = []
        for led_name in [
            "led",
            "led_phong_khach",
            "led_phong_ba_me",
            "led_phong_con_trai",
            "led_bep",
        ]:
            responses.append(turn_on_led(led_name))
        response = "Đã bật tất cả đèn"
    else:
        response = f"Không hiểu lệnh: '{text}'"

    log_speech(f"👉 Phản hồi: {response}")  # Ghi phản hồi vào file log
    return response
