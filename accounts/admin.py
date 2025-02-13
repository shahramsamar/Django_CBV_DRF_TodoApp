from django.contrib import admin
from django.contrib.auth.admin import UserAdmin
from .models import User, Profile

# Extend Django's default UserAdmin to support your custom user model
class CustomUserAdmin(UserAdmin):
    model = User
    fieldsets = UserAdmin.fieldsets + (  # Add additional fields to the admin panel
        (None, {"fields": ("user_picture",)}),
    )
    add_fieldsets = UserAdmin.add_fieldsets + (
        (None, {"fields": ("user_picture",)}),
    )

# Register Profile model
class ProfileAdmin(admin.ModelAdmin):
    list_display = ('user', 'first_name', 'last_name', 'created_date')
    search_fields = ('user__username', 'first_name', 'last_name')
    ordering = ('-created_date',)

admin.site.register(User, CustomUserAdmin)
admin.site.register(Profile, ProfileAdmin)
