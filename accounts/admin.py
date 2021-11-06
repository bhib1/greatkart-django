from django.contrib import admin
from django.contrib.auth.admin import UserAdmin
from .models import Account


class AccountAdmin(UserAdmin):
    list_display = ('email', 'first_name', 'last_name', 'username', 'last_login', 'date_joined', 'is_active')
    list_display_links = ('email', 'first_name', 'last_name')
    readonly_fields = ('last_login', 'date_joined')
    # اردر باید تاپل یا لیست باشه یا اون , مشخص کردیم که یک تاپل است
    ordering = ('date_joined',)

    filter_horizontal = ()
    list_filter = ()
    # این باعث میشه پاسورد read-only بشه
    fieldsets = ()


admin.site.register(Account, AccountAdmin)
