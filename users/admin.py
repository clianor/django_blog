from django.contrib import admin
from .models import User


@admin.register(User)
class UserAdmin(admin.ModelAdmin):
    def is_admin_icon(self, obj):
        return obj.is_admin
    is_admin_icon.boolean = True
    is_admin_icon.short_description = '관리자'

    list_display = ['email', 'username', 'is_admin_icon']
