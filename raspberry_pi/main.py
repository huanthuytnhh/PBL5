from voice.speech_recognition import process_command, recognize_speech


def main():
    print("Chương trình điều khiển LED bằng giọng nói (Phiên bản test)")
    print("Nói 'bật đèn', 'tắt đèn' hoặc 'chuyển đèn' để điều khiển")

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
                break

        except KeyboardInterrupt:
            print("\nĐã dừng chương trình")
            break


if __name__ == "__main__":
    main()
