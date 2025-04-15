# 🏠 Smart Home System – Django Project Structure & Best Practices

## 📌 Mục tiêu dự án

Hệ thống nhà thông minh cho phép:

- Quản lý **thành viên** trong nhà.
- Quản lý **thiết bị** như đèn, cửa, cảm biến...
- Gán **quyền điều khiển thiết bị** cho từng thành viên.
- Hiển thị thiết bị tương ứng với người dùng đã đăng nhập.

---

## 📁 Cấu trúc thư mục

```
smart_home/
├── smart_home/          # Cấu hình chính của Django project
│   ├── __init__.py
│   ├── settings.py
│   ├── urls.py
│   └── wsgi.py
├── home/                # App chính: quản lý thành viên, thiết bị, phân quyền
│   ├── admin.py
│   ├── apps.py
│   ├── models.py
│   ├── views.py
│   ├── urls.py
│   ├── templates/       # Template HTML
│   │   └── home/
│   │       └── dashboard.html
│   └── static/          # CSS/JS
├── db.sqlite3           # CSDL mặc định (có thể dùng PostgreSQL sau)
└── manage.py
```

---

## 🧠 Mô hình dữ liệu (models.py)

```python
from django.db import models
from django.contrib.auth.models import User

class Appliance(models.Model):
    name = models.CharField(max_length=100)

    def __str__(self):
        return self.name

class Member(models.Model):
    user = models.OneToOneField(User, on_delete=models.CASCADE)
    full_name = models.CharField(max_length=100)

    def __str__(self):
        return self.full_name

class Permission(models.Model):
    member = models.ForeignKey(Member, on_delete=models.CASCADE)
    appliance = models.ForeignKey(Appliance, on_delete=models.CASCADE)

    def __str__(self):
        return f"{self.member.full_name} → {self.appliance.name}"
```

## ⚙️ Quản trị viên (admin.py)

```python
from django.contrib import admin
from .models import Appliance, Member, Permission

@admin.register(Appliance)
class ApplianceAdmin(admin.ModelAdmin):
    list_display = ('name',)

@admin.register(Member)
class MemberAdmin(admin.ModelAdmin):
    list_display = ('full_name',)

@admin.register(Permission)
class PermissionAdmin(admin.ModelAdmin):
    list_display = ('member', 'appliance')
    list_filter = ('member', 'appliance')
```

## 🖥️ Giao diện người dùng cơ bản

### views.py
```python
from django.shortcuts import render
from .models import Permission

def dashboard(request):
    member = request.user.member
    permissions = Permission.objects.filter(member=member)
    return render(request, 'home/dashboard.html', {'permissions': permissions})
```

### dashboard.html
```html
<h2>Danh sách thiết bị bạn được điều khiển:</h2>
<ul>
  {% for p in permissions %}
    <li>{{ p.appliance.name }}</li>
  {% endfor %}
</ul>
```

## ✅ Best Practices

- 🔐 Tách logic phân quyền rõ ràng qua model Permission.
- 🧩 Sử dụng Django Admin để tạo dữ liệu nhanh, dễ test.
- 🔍 Filter dữ liệu theo request.user để bảo mật thiết bị.
- 🧪 Viết test đơn giản cho các model và view chính.
- 🔄 Có thể mở rộng thành REST API (sau khi hoàn thiện giao diện).
- 📱 Có thể kết nối Mobile App (Flutter, React Native...) với Django API.

## 🚀 Gợi ý mở rộng

- Thêm trạng thái cho thiết bị (is_on, temperature, v.v).
- Giao diện điều khiển thiết bị bằng AJAX hoặc WebSocket.
- Ghi lại lịch sử điều khiển thiết bị.
- Phân loại phòng (Room) chứa thiết bị.

## 📚 Công nghệ sử dụng

- Backend: Django
- Frontend: Django Template (có thể nâng cấp React/Vue)
- Database: SQLite (dev) → PostgreSQL (prod)
- Auth: Django Auth + User Profile (Member) + Voice Recognition (LSTM)

## 🎤 Tích hợp Nhận dạng Giọng nói

```python
# views.py trong app api
from ai_model.inference import predict_speaker
from django.http import JsonResponse

def identify_user(request):
    if request.method == 'POST' and request.FILES.get('audio'):
        audio_file = request.FILES['audio']
        # Lưu file tạm
        temp_path = 'temp_audio.wav'
        with open(temp_path, 'wb+') as f:
            for chunk in audio_file.chunks():
                f.write(chunk)

        # Dự đoán người dùng
        speaker, confidence, _ = predict_speaker(temp_path)

        # Tìm member tương ứng
        try:
            member = Member.objects.get(user__username=speaker)
            return JsonResponse({
                'success': True,
                'user_id': member.user.id,
                'username': speaker,
                'confidence': confidence
            })
        except Member.DoesNotExist:
            return JsonResponse({
                'success': False,
                'message': 'Không tìm thấy người dùng'
            })

    return JsonResponse({'success': False, 'message': 'Yêu cầu không hợp lệ'})
```

## 🔌 Tích hợp với Raspberry Pi và ESP32

```python
# models.py - Thêm vào models hiện có
class Device(models.Model):
    DEVICE_TYPES = [
        ('led', 'LED'),
        ('door', 'Door'),
        ('sensor', 'Sensor'),
        ('switch', 'Switch'),
    ]

    name = models.CharField(max_length=100)
    device_type = models.CharField(max_length=10, choices=DEVICE_TYPES)
    room = models.ForeignKey('Room', on_delete=models.CASCADE)
    is_on = models.BooleanField(default=False)
    ip_address = models.GenericIPAddressField(null=True, blank=True)  # Cho ESP32
    gpio_pin = models.IntegerField(null=True, blank=True)  # Cho Raspberry Pi

    def __str__(self):
        return f"{self.name} ({self.room.name})"

class Room(models.Model):
    name = models.CharField(max_length=100)

    def __str__(self):
        return self.name

class DeviceLog(models.Model):
    device = models.ForeignKey(Device, on_delete=models.CASCADE)
    user = models.ForeignKey(Member, on_delete=models.CASCADE)
    timestamp = models.DateTimeField(auto_now_add=True)
    action = models.CharField(max_length=100)

    def __str__(self):
        return f"{self.user} {self.action} {self.device} at {self.timestamp}"
```

## 🔄 API cho Mobile App và Raspberry Pi

```python
# urls.py trong app api
from django.urls import path
from . import views

urlpatterns = [
    path('devices/', views.DeviceListView.as_view(), name='device-list'),
    path('devices/<int:pk>/', views.DeviceDetailView.as_view(), name='device-detail'),
    path('devices/<int:pk>/control/', views.DeviceControlView.as_view(), name='device-control'),
    path('identify/', views.identify_user, name='identify-user'),
]
```

## 📱 Tích hợp Mobile App

Sử dụng REST API để kết nối với Mobile App:

1. Đăng nhập qua REST API hoặc nhận dạng giọng nói
2. Lấy danh sách thiết bị của người dùng
3. Điều khiển thiết bị từ xa thông qua API

## 🚀 Gợi ý mở rộng

- Tích hợp thêm mô hình nhận dạng lệnh giọng nói (NLP)
- Thêm trạng thái và theo dõi thiết bị theo thời gian thực (WebSocket)
- Thêm tính năng lập lịch tự động điều khiển thiết bị
- Thêm chế độ tiết kiệm năng lượng dựa trên thói quen người dùng

---

Với cấu trúc trên, hệ thống Smart Home sẽ đầy đủ các tính năng: quản lý người dùng, quản lý thiết bị, nhận dạng giọng nói, kết nối Raspberry Pi và ESP32, và cung cấp API cho Mobile App.
