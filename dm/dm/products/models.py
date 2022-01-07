# Django
from django.db import models

# Own
from vendors.models import Vendor
from utils.normalize import normalize_text


def upload_img(instance, filename):

    vendor_name = instance.vendor.name.lower().replace(" ", "-")

    return f'img/{vendor_name}/{filename}'


def upload_img_webp(instance, filename):

    vendor_name = instance.vendor.name.lower().replace(" ", "-")

    return f'img/{vendor_name}/{filename}'


class Brand(models.Model):

    brand = models.CharField("Brand", max_length=50)

    class Meta:
        verbose_name = "Brand"
        verbose_name_plural = "Brands"

    def save(self, *args, **kwargs):

        self.brand = self.brand.upper()

        super(__class__, self).save(*args, **kwargs)

    def __str__(self):
        return self.brand


class Category(models.Model):

    category = models.CharField("Category", max_length=30)

    class Meta:
        verbose_name = "Category"
        verbose_name_plural = "Categories"

    def save(self, *args, **kwargs):

        self.category = self.category.lower().capitalize()

        super(__class__, self).save(*args, **kwargs)

    def __str__(self):
        return self.category


class Product(models.Model):

    code = models.CharField("Product code", max_length=20)
    name = models.CharField("Name", max_length=50)
    normalized_name = models.CharField("Name", max_length=50, blank=True)
    description = models.TextField("Description",  null=True, blank=True)

    stock = models.SmallIntegerField("Cantidad disponible", null=True)
    in_stock = models.BooleanField("In stock", default=True)
    category = models.ManyToManyField(Category)
    vendor = models.ForeignKey(Vendor, on_delete=models.CASCADE)
    vendor_code = models.CharField("Vendor code", max_length=25)
    brand = models.ForeignKey(
        Brand, on_delete=models.CASCADE, null=True, blank=True)
    price = models.DecimalField("Price", max_digits=7, decimal_places=2)

    img = models.ImageField("Image", upload_to=upload_img, null=True)
    img_webp = models.ImageField(
        "Image WEBP", upload_to=upload_img_webp, null=True)

    class Meta:
        verbose_name = "Product"
        verbose_name_plural = "Products"
        indexes = [
            models.Index(fields=['code']),
            models.Index(fields=['code'], name='product_code_idx')
        ]

    @property
    def Name(self):
        if self.brand:
            return '({}) - {} | {}'.format(
                self.vendor_code,
                self.name,
                self.brand
            )
        else:
            return '({}) - {}'.format(self.vendor_code, self.name)

    def __add_code(self):

        list_code = __class__.objects.values_list("code", flat=True)

        reference = max(list_code)

        self.code = reference + 1

    def __add_normalized_name(self):

        self.normalized_name = normalize_text(self.name)

    def initial_pre_save(self):
        """ Pre save when the instance is created """

        self.__add_code()
        self.__add_normalized_name()

    def save(self, *args, **kwargs):

        created = True if self._state.adding else False

        if created:
            self.initial_pre_save()
        self.__add_normalized_name()
        super(__class__, self).save(*args, **kwargs)

    def __str__(self):
        return self.Name
