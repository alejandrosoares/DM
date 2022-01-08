# Django
from django.contrib import admin

# Own
from .models import Brand, Category, Product


class BrandAdmin(admin.ModelAdmin):
    list_display = ('brand',)
    fields = ('brand',)


admin.site.register(Brand, BrandAdmin)


class CategoryAdmin(admin.ModelAdmin):
    list_display = ('category',)
    fields = ('category',)


admin.site.register(Category, CategoryAdmin)


class ProductAdmin(admin.ModelAdmin):
    list_display = ('name', 'code', 'in_stock', 'stock')
    fields = (
        'code', 'name', 'in_stock', 'stock', 'description',
        'img', 'category', 'vendor', 'vendor_code', 'price',
        'brand', 'brand_name'
    )
    readonly_fields = ('code', 'brand_name')
    search_fields = ['name', 'code']
    list_filter = ('vendor__name',)


admin.site.register(Product, ProductAdmin)
