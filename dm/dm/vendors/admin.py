from django.contrib import admin

from .models import Vendor, LeadTimeVendors


class VendorAdmin(admin.ModelAdmin):
    list_display = ('name',)
    fields = ('name', 'contact', 'average_lead_time',
              'max_lead_time', 'min_lead_time')
    readonly_fields = ('average_lead_time', 'max_lead_time', 'min_lead_time')


admin.site.register(Vendor, VendorAdmin)


class LeadTimeVendorsAdmin(admin.ModelAdmin):
    list_display = ('vendor',)
    fields = ('vendor', 'lead_time')


admin.site.register(LeadTimeVendors, LeadTimeVendorsAdmin)
