from django.contrib import admin
from .models import Driver


# اکشن تایید راننده
def approve_driver(modeladmin, request, queryset):
    queryset.update(approved=True)


approve_driver.short_description = "تایید راننده‌های انتخاب شده"


class DriverAdmin(admin.ModelAdmin):
    list_display = ('username', 'name', 'phone', 'approved')

    search_fields = ('username', 'name', 'phone')

    list_filter = ('approved',)

    list_editable = ('approved',)

    actions = [approve_driver]


admin.site.register(Driver, DriverAdmin)
