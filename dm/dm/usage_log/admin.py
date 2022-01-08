from django.contrib import admin

from .models import QueriesLog, CategoryLog, ProductLog


class QueriesLogAdmin(admin.ModelAdmin):
    list_display = ('date', 'query')
    fields = ('date', 'query')
    readonly_fields = ('date', 'query')


admin.site.register(QueriesLog, QueriesLogAdmin)


class CategoryLogAdmin(admin.ModelAdmin):
    list_display = ('date', 'category', 'quantity')
    fields = ('date', 'category', 'quantity')
    readonly_fields = ('date', 'category', 'quantity')


admin.site.register(CategoryLog, CategoryLogAdmin)


class ProductLogAdmin(admin.ModelAdmin):
    list_display = ('date', 'product', 'quantity')
    fields = ('date', 'product', 'quantity')
    readonly_fields = ('date', 'product', 'quantity')


admin.site.register(ProductLog, ProductLogAdmin)
