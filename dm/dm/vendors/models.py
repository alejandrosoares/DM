from django.db import models
from django.db.models import Max, Avg, Min
from django.db.models.signals import pre_save, post_save
from django.dispatch import receiver

class Vendor(models.Model):
	name = models.CharField(verbose_name="Nombre", max_length=50)
	contactInformation =  models.TextField(verbose_name="Informacion de contacto")
	averageLeadTime = models.DecimalField(
		verbose_name="Tiempo de entrega promedio (en dias)", 
		max_digits=4, decimal_places=1, 
		null=True
		)
	maxLeadTime = models.DecimalField(verbose_name="Tiempo de entrega maximo  (en dias)", max_digits=4, decimal_places=1, null=True)
	minLeadTime = models.DecimalField(verbose_name="Tiempo de entrega minimo  (en dias)", max_digits=4, decimal_places=1, null=True)

	class Meta:
		verbose_name = "Proveedor"
		verbose_name_plural = "Proveedores"


	def __str__(self):
		return self.name


class LeadTimeVendors(models.Model):
	leadTime = models.DecimalField(verbose_name="Tiempo de entrega (en dias)", max_digits=4, decimal_places=1)
	vendor = models.ForeignKey(Vendor, on_delete=models.CASCADE)

	class Meta:
		verbose_name = "Tiempo de entrega"
		verbose_name_plural = "Tiempos de entrega"


	@property
	def Name(self):
		return '{}'.format(self.vendor.name)
	

	def __str__(self):
		return self.Name


@receiver(pre_save, sender=Vendor)
def PreSaveVendor(sender, instance, **kwargs):
	instance.name = instance.name.upper()


@receiver(pre_save, sender=LeadTimeVendors)
def PreSaveLeadTimeVendors(sender, instance, **kwargs):
	if instance.vendor.averageLeadTime == None:
		instance.vendor.averageLeadTime = instance.leadTime
	
	if instance.vendor.maxLeadTime == None:
		instance.vendor.maxLeadTime = instance.leadTime

	if instance.vendor.minLeadTime == None:
		instance.vendor.minLeadTime = instance.leadTime
	
	instance.vendor.save()


@receiver(post_save, sender=LeadTimeVendors)
def PostSaveLeadTimeVendors(sender, instance, **kwargs):
	
	dicQuery = LeadTimeVendors.objects.filter(vendor__id=instance.vendor.id).aggregate(Avg('leadTime'))
	instance.vendor.averageLeadTime = dicQuery['leadTime__avg']

	dicQuery = LeadTimeVendors.objects.filter(vendor__id=instance.vendor.id).aggregate(Max('leadTime'))
	instance.vendor.maxLeadTime = dicQuery['leadTime__max']

	dicQuery = LeadTimeVendors.objects.filter(vendor__id=instance.vendor.id).aggregate(Min('leadTime'))
	instance.vendor.minLeadTime = dicQuery['leadTime__min']

	instance.vendor.save()

