# Django
from django.contrib import admin

# Own
from .models import Brand, Category, Product


class BrandAdmin(admin.ModelAdmin):
    list_display = ('brand',)
    fields = ('brand',)


admin.site.register(Brand, BrandAdmin)


class CategoryAdmin(admin.ModelAdmin):
    list_display = ('category', 'num_products')
    fields = ('category', 'num_products')
    readonly_fields = ('num_products',)


admin.site.register(Category, CategoryAdmin)


class ProductAdmin(admin.ModelAdmin):
    list_display = ('name', 'code', 'in_stock', 'stock')
    fields = (
        'code', 'name', 'load_img',  'in_stock', 'stock', 'description',
        'img', 'img_small', 'img_webp', 'img_small_webp', 'categories', 'vendor', 'vendor_code', 'price',
        'brand', 'brand_name'
    )
    readonly_fields = ('code', 'brand_name')
    search_fields = ['name', 'code']
    list_filter = ('vendor__name',)


admin.site.register(Product, ProductAdmin)
