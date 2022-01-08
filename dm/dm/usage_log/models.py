# Django
from django.db import models
from django.db.models.signals import post_save
from django.dispatch import receiver

# Own
from products.models import Category, Product, Brand

# Thrid parties

from datetime import datetime


class QueriesLog(models.Model):
    """ Log the queries performed through input search """

    query = models.CharField("Consulta realizada", max_length=50)
    date = models.DateTimeField(
        "Created", auto_now_add=True, auto_now=False)

    class Meta:
        verbose_name = "Consulta"
        verbose_name_plural = "Consultas"


class CategoryLog(models.Model):
    """ Log for day the use of categories """

    category = models.ForeignKey(Category, on_delete=models.CASCADE)
    quantity = models.PositiveIntegerField("Cantidad", default=0)
    date = models.DateField("Created", auto_now_add=True, auto_now=False)

    class Meta:
        verbose_name = "Categoria consultada"
        verbose_name_plural = "Categorias consultas"

    def increase_quantity_field(self):
        self.quantity += 1
        self.save()

    @staticmethod
    def create_log(category):
        date = datetime.now().date()
        log, _ = __class__.objects.get_or_create(
            category=category,
            date=date
        )
        log.increase_quantity_field()

    class Meta:
        verbose_name = "Uso de categoria"
        verbose_name_plural = "Uso de categorias"
        ordering = ['-quantity']

    def __str__(self):
        return self.category.category


class ProductLog(models.Model):
    """Log products of interest"""

    product = models.ForeignKey(Product, on_delete=models.CASCADE)
    quantity = models.PositiveIntegerField("Cantidad", default=0)
    date = models.DateField("Created", auto_now_add=True, auto_now=False)

    class Meta:
        verbose_name = "Producto consultado"
        verbose_name_plural = "Productos consultos"

    def increase_quantity_field(self):
        self.quantity += 1
        self.save()

    @staticmethod
    def create_log(product):
        date = datetime.now().date()
        log, _ = __class__.objects.get_or_create(
            product=product,
            date=date
        )
        log.increase_quantity_field()

    def __str__(self):
        return self.product.name
