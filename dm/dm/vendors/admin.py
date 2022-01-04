from django.contrib import admin

from .models import Vendor, LeadTimeVendors

class VendorAdmin(admin.ModelAdmin):
	list_display = ('name',)
	fields = ('name','contactInformation','averageLeadTime','maxLeadTime','minLeadTime')
	readonly_fields = ('averageLeadTime','maxLeadTime','minLeadTime')

admin.site.register(Vendor, VendorAdmin)


class LeadTimeVendorsAdmin(admin.ModelAdmin):
	list_display = ('vendor',)
	fields = ('vendor','leadTime')

admin.site.register(LeadTimeVendors, LeadTimeVendorsAdmin)