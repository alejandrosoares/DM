from django.db import models
from django.db.models import Max, Avg, Min
from django.db.models.signals import pre_save, post_save
from django.dispatch import receiver


class Vendor(models.Model):
    """Vendor Model"""

    name = models.CharField("Nombre", max_length=50)
    contact = models.TextField("Informacion de contacto")
    average_lead_time = models.DecimalField(
        "Tiempo de entrega promedio (en dias)",
        max_digits=4,
        decimal_places=1,
        null=True
    )
    max_lead_time = models.DecimalField(
        "Tiempo de entrega maximo  (en dias)",
        max_digits=4,
        decimal_places=1,
        null=True
    )
    min_lead_time = models.DecimalField(
        "Tiempo de entrega minimo  (en dias)",
        max_digits=4,
        decimal_places=1,
        null=True
    )

    class Meta:
        verbose_name = "Proveedor"
        verbose_name_plural = "Proveedores"

    def set_lead_time(self, lead_time):
        """Set the fields:
            -average_lead_time
            -max_lead_time
            -min_lead_time
        """

        if self.average_lead_time == None:
            self.average_lead_time = lead_time

        if self.max_lead_time == None:
            self.max_lead_time = lead_time

        if self.min_lead_time == None:
            self.min_lead_time = lead_time

        self.save()

    def update_fields(self, dic_fields):
        """Update fields:
            -average_lead_time
            -max_lead_time
            -min_lead_time
        """

        self.average_lead_time = dic_fields['average']
        self.max_lead_time = dic_fields['max']
        self.min_lead_time = dic_fields['min']
        self.save()

    def __str__(self):
        return self.name


class LeadTimeVendors(models.Model):
    lead_time = models.DecimalField(
        "Tiempo de entrega (en dias)",
        max_digits=4,
        decimal_places=1
    )
    vendor = models.ForeignKey(
        Vendor,
        on_delete=models.CASCADE,
        related_name='lead_times'
    )

    class Meta:
        verbose_name = "Tiempo de entrega"
        verbose_name_plural = "Tiempos de entrega"

    @property
    def Name(self):
        return '{}'.format(self.vendor.name)

    def __str__(self):
        return self.Name


@receiver(pre_save, sender=Vendor)
def presave_vendor(sender, instance, **kwargs):
    """Pre Save Vendor"""

    instance.name = instance.name.upper()


@receiver(pre_save, sender=LeadTimeVendors)
def presave_LeadTimeVendors(sender, instance, **kwargs):
    """Pre save LeadTimeVendors"""

    instance.vendor.set_lead_time(instance.lead_time)


@receiver(post_save, sender=LeadTimeVendors)
def postsave_LeadTimeVendors(sender, instance, **kwargs):
    """Post Save LeadTimeVendors"""

    lead_times = sender.objects.filter(
        vendor__id=instance.vendor.id
    )

    query = lead_times.aggregate(
        average=Avg('lead_time'),
        max=Max('lead_time'),
        min=Min('lead_time')
    )

    instance.vendor.update_fields(query)
