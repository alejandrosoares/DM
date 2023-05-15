from django.contrib import admin

from .models import Brand, Category, Product


class BrandAdmin(admin.ModelAdmin):
    list_display = ('name',)
    fields = ('name',)


class CategoryAdmin(admin.ModelAdmin):
    list_display = ('name', 'num_products')
    fields = ('name', 'num_products', 'enable')
    readonly_fields = ('num_products',)


class ProductAdmin(admin.ModelAdmin):
    list_display = ('name', 'code', 'in_stock', 'stock')
    fields = (
        'code', 'name',  'in_stock', 'stock', 'description',
        'img', 'img_webp', 'img_small_webp', 'categories', 
        'price', 'brand'
    )
    readonly_fields = ('code',)
    search_fields = ['name', 'code']


admin.site.register(Brand, BrandAdmin)
admin.site.register(Category, CategoryAdmin)
admin.site.register(Product, ProductAdmin)
