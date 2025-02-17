from django.contrib import admin
from django.contrib.auth.admin import UserAdmin
from .models import User, Profile

# Extend Django's default UserAdmin to support your custom user model
class CustomUserAdmin(UserAdmin):
    model = User

    fieldsets = (
        (None, {"fields": ("email", "password", "user_picture")}),
        ("Permissions", {"fields": ("is_staff", "is_active")}),
    )

    add_fieldsets = (
        (None, {
            "classes": ("wide",),
            "fields": ("email", "password1", "password2", "user_picture", "is_staff", "is_active"),
        }),
    )

    list_display = ("email", "is_staff", "is_active")  # Removed username
    search_fields = ("email",)  # Removed username
    ordering = ("email",)  # Changed from username to email

# Register Profile model
class ProfileAdmin(admin.ModelAdmin):
    list_display = ('user', 'first_name', 'last_name', 'created_date')
    search_fields = ('user__email', 'first_name', 'last_name')  # Changed username to email
    ordering = ('-created_date',)

admin.site.register(User, CustomUserAdmin)
admin.site.register(Profile, ProfileAdmin)
