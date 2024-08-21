from django.contrib import admin
from .models import Products, Discount


class ProductAdmin(admin.ModelAdmin):
    list_display = ('name', 'price', 'stock')
    list_filter = ('name', 'price', 'stock')


class DiscountAdmin(admin.ModelAdmin):
    list_display = ('code', 'discount', 'expire_date')


admin.site.register(Products, ProductAdmin)
admin.site.register(Discount, DiscountAdmin)