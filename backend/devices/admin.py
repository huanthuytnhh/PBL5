from django.contrib import admin
from .models import Device

class DeviceAdmin(admin.ModelAdmin):
    # Hiển thị các trường này trong danh sách thiết bị
    list_display = ('name', 'device_type', 'is_on', 'gpio_pin', 'ip_address')
    # Cho phép lọc theo các trường này
    list_filter = ('device_type', 'is_on')
    # Các trường hiển thị trong form thêm/sửa
    fields = ['name', 'device_type', 'is_on', 'gpio_pin', 'ip_address']
    # Thêm thanh tìm kiếm theo tên
    search_fields = ['name']

# Đăng ký model Device với lớp cấu hình DeviceAdmin
admin.site.register(Device, DeviceAdmin)
