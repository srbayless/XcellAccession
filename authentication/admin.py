from django.contrib import admin
from django.contrib.auth.admin import UserAdmin
from authentication.models import UserModel


class XCellAdmin(UserAdmin):
    list_display = (
        'username', 'first_name', 'last_name', 'password', 'title', 'department', 'avatar_image'
    )
    fieldsets = (
        (None, {
            'fields': ('username', 'password', 'first_name', 'last_name', 'title', 'department', 'avatar_image')
        }),
        ('Permissions', {
            'fields': (
                'is_active', 'is_staff', 'is_superuser',
                'groups', 'user_permissions'
                )
        }),
        ('Important dates', {
            'fields': ('last_login', 'date_joined')
        }),
    )

    add_fieldsets = (
        (None, {
            'fields': ('username', 'password1', 'password2', 'first_name', 'last_name', 'title', 'department', 'avatar_image')
        }),
        ('Permissions', {
            'fields': (
                'is_active', 'is_staff', 'is_superuser',
                'groups', 'user_permissions'
                )
        }),
        ('Important dates', {
            'fields': ('last_login', 'date_joined')
        }),
    )

admin.site.register(UserModel, XCellAdmin)

# Register your models here.
