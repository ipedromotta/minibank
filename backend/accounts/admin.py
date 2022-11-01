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
    
class TransactionsAdmin(admin.ModelAdmin):
    model = Transactions
    list_display = ('user', 'amount', 'type', 'created_at', )
    search_fields = ('user__username', )
    list_filter = ('type', 'created_at', )
    

admin.site.register(CustomUser, CustomUserAdmin)
admin.site.register(Transactions, TransactionsAdmin)
