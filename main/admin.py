from django.contrib import admin
from django.contrib.auth.models import Group
from django.contrib.sites.models import Site
from .models import CustomUser
from django.contrib.auth.admin import UserAdmin


class CustomUserAdmin(UserAdmin):
    fieldsets = (
        (None, {'fields': ('username', 'email', 'password')}),
        ('Permissions', {'fields': ('is_active', 'is_staff', 'is_superuser', 'groups', 'user_permissions')}),
    )
    add_fieldsets = (
        (None, {'classes': ('wide',), 'fields': ('username', 'email', 'password1', 'password2')}),
    )


admin.site.register(CustomUser, CustomUserAdmin)
admin.site.unregister(Group)
admin.site.unregister(Site)
