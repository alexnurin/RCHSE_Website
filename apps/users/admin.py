from django.contrib import admin
from .models import User
from django.contrib.auth.admin import UserAdmin

class CustomUserAdmin(UserAdmin):
    fieldsets = UserAdmin.fieldsets + (
        (None, {'fields': ('is_admin',)}),
    )
    list_display = UserAdmin.list_display + ('is_admin',)


admin.site.register(User, CustomUserAdmin)
