from django.contrib import admin

from .models import Product, Category, Brand


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
		'code','name', 'in_stock', 'stock','description',
		'img','category', 'vendor','vendor_code', 'price',
	)
	readonly_fields = ('code',)
	search_fields = ['name','code']
	list_filter = ('vendor__name',)

admin.site.register(Product, ProductAdmin)

