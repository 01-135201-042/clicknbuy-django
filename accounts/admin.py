from django.contrib import admin
from django.contrib.auth.admin import UserAdmin

# Register your models here.

from .models import Account

class AccountAdmin(UserAdmin):
    list_display = ('email', 'first_name', 'last_name', "username", 'last_login','date_joined', "is_active")
    
    filter_horizontal = ()
    list_filter = ()
    fieldsets = ()

admin.site.register(Account, AccountAdmin)