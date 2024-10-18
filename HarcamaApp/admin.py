from django.contrib import admin
from .models import Expense

@admin.register(Expense)
class ExpenseAdmin(admin.ModelAdmin):
    list_display = ('timestamp', 'user', 'kalem', 'kart', 'fiyat')
    list_filter = ('timestamp', 'user', 'kalem', 'kart')
    search_fields = ('user__username', 'kalem', 'kart')
    date_hierarchy = 'timestamp'
    ordering = ('-timestamp',)

    fieldsets = (
        ('Basic Information', {
            'fields': ('user', 'timestamp')
        }),
        ('Expense Details', {
            'fields': ('kalem', 'kart', 'fiyat')
        }),
    )

    def get_readonly_fields(self, request, obj=None):
        if obj:  # editing an existing object
            return 'timestamp', 'user'
        return ()