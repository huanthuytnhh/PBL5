#!/bin/bash

echo "🔄 Đang cập nhật hệ thống..."
sudo apt update -y

echo "🛠️ Cài đặt các gói hệ thống bằng APT..."
sudo apt install -y python3-django python3-gpiozero portaudio19-dev flac

echo "🐍 Cài đặt các thư viện Python bằng pip..."
pip install --break-system-packages djangorestframework speechrecognition pyaudio

echo "✅ Hoàn thành! Kiểm tra các thư viện..."
python3 -c "import django; print('✅ Django:', django.get_version())"
python3 -c "import gpiozero; print('✅ GPIOZero OK!')"
python3 -c "import speech_recognition; print('✅ SpeechRecognition OK!')"
python3 -c "import pyaudio; print('✅ PyAudio OK!')"

echo "🚀 Mọi thứ đã sẵn sàng!"
