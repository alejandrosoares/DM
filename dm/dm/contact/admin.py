from django.contrib import admin

from .models import Contact

class ContactAdmin(admin.ModelAdmin):
	list_display = ('name', 'date')
	readonly_fields = ['name', 'date', 'email', 'phone', 'message','user']

admin.site.register(Contact, ContactAdmin)

