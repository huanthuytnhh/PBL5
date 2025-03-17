import subprocess
import sys


def install_dependencies():
    """Cài đặt các thư viện cần thiết"""
    dependencies = ["gpiozero", "SpeechRecognition", "pyaudio", "requests", "RPi.GPIO"]

    print("Đang cài đặt các thư viện cần thiết...")
    for package in dependencies:
        print(f"Đang cài đặt {package}...")
        subprocess.check_call([sys.executable, "-m", "pip", "install", package])

    print("Đã cài đặt xong các thư viện cần thiết!")


if __name__ == "__main__":
    install_dependencies()
