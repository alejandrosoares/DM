from django.contrib import admin

from .models import Contact, ContactInformation


class ContactAdmin(admin.ModelAdmin):
	list_display = ('name', 'date')
	readonly_fields = ['name', 'date', 'email', 'phone', 'message']


admin.site.register(Contact, ContactAdmin)
admin.site.register(ContactInformation)


