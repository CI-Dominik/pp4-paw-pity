from django.contrib import admin
from django.contrib.auth.models import Group
from django.contrib.sites.models import Site
from django.contrib.auth.admin import UserAdmin
from .models import CustomUser

# Register your models here.
admin.site.register(CustomUser, UserAdmin)
admin.site.unregister(Group)
admin.site.unregister(Site)
