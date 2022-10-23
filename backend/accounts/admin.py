from django.contrib import admin

from django.contrib.auth.admin import UserAdmin

from .models import CustomUser, Transactions

class CustomUserAdmin(UserAdmin):
    list_display = (
        'username', 'email', 'first_name', 'last_name', 'is_staff',
        'balance'
        )
    
    fieldsets = (
        (None, {
            'fields': ('username', 'password')
        }),
        ('Personal info', {
            'fields': ('first_name', 'last_name', 'email', 'balance')
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
        # ('Additional info', {
        #     'fields': ('is_student', 'is_teacher', 'mailing_address')
        # })
    )

admin.site.register(CustomUser, CustomUserAdmin)
admin.site.register(Transactions)
