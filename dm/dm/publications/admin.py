from django.contrib import admin

from .models import  Publication

class PublicationAdmin(admin.ModelAdmin):
	list_display = ('name', 'created')
	fields = ('name','code', 'created','visits', 'link', 'shorten_link', 'short_link', 'products')
	readonly_fields = ('code', 'created','visits', 'link')

admin.site.register(Publication, PublicationAdmin)