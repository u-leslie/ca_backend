from django.contrib import admin
from .models import MenuItem, Table, Order, OrderItem


@admin.register(MenuItem)
class MenuItemAdmin(admin.ModelAdmin):
    list_display = ('name', 'price', 'stock')
    search_fields = ('name',)
    list_editable = ('price', 'stock')


@admin.register(Table)
class TableAdmin(admin.ModelAdmin):
    list_display = ('number', 'seats', 'is_reserved')
    list_filter = ('is_reserved',)
    list_editable = ('is_reserved',)


class OrderItemInline(admin.TabularInline):
    model = OrderItem
    extra = 0


@admin.register(Order)
class OrderAdmin(admin.ModelAdmin):
    list_display = ('id', 'table', 'total', 'created_at')
    inlines = [OrderItemInline]
    readonly_fields = ('total', 'created_at')