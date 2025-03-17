import speech_recognition as sr


def list_microphones():
    """Liệt kê tất cả microphone được phát hiện"""
    print("Danh sách microphone được phát hiện:")
    for index, name in enumerate(sr.Microphone.list_microphone_names()):
        print(f"Microphone {index}: {name}")


def test_microphone(device_index=None):
    """Test microphone cụ thể"""
    recognizer = sr.Recognizer()

    try:
        with sr.Microphone(device_index=device_index) as source:
            print(
                f"Đang test microphone {device_index if device_index is not None else 'mặc định'}"
            )
            print("Hãy nói gì đó...")
            audio = recognizer.listen(source, timeout=5)
            print("Đã ghi âm xong, đang xử lý...")

            text = recognizer.recognize_google(audio, language="vi-VN")
            print(f"Đã nhận diện: '{text}'")
            return True
    except sr.WaitTimeoutError:
        print("Không phát hiện giọng nói trong 5 giây")
        return False
    except sr.UnknownValueError:
        print("Không thể nhận diện được giọng nói")
        return False
    except sr.RequestError as e:
        print(f"Lỗi khi gửi yêu cầu đến Google Speech Recognition: {e}")
        return False
    except Exception as e:
        print(f"Lỗi: {e}")
        return False


if __name__ == "__main__":
    # Liệt kê tất cả microphone
    list_microphones()

    # Test microphone mặc định
    if not test_microphone():
        # Nếu microphone mặc định không hoạt động, thử từng microphone khác
        print("\nThử từng microphone khác...")
        for i in range(len(sr.Microphone.list_microphone_names())):
            if test_microphone(i):
                print(f"\nMicrophone {i} hoạt động tốt!")
                print(f"Hãy sử dụng index này trong file speech_recognition.py")
                break
