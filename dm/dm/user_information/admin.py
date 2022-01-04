from django.contrib import admin

from .models import Queries, UseOfCategories, SearchWords, Publications

class QueriesAdmin(admin.ModelAdmin):
	list_display = ('query',)
	readonly_fields = ('query',)
admin.site.register(Queries, QueriesAdmin)

class UseOfCategoriesAdmin(admin.ModelAdmin):
	list_display = ('category','quantity')
	readonly_fields = ('category','quantity',)
admin.site.register(UseOfCategories, UseOfCategoriesAdmin)

class SearchWordsAdmin(admin.ModelAdmin):
	list_display = ('string','quantity')
	readonly_fields = ('string','quantity','idObject','typeString','img')
admin.site.register(SearchWords, SearchWordsAdmin)


class PublicationsAdmin(admin.ModelAdmin):
	list_display = ('code','name')
	fields = ('name','code', 'datetime','numberOfVisites', 'shortLink', 'longLink', 'products')
	readonly_fields = ('code', 'datetime','numberOfVisites', 'shortLink', 'longLink')
admin.site.register(Publications, PublicationsAdmin)

