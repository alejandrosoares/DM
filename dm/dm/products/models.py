# Django
from ctypes.wintypes import SIZE
from pickletools import optimize
from django.db import models
from django.db.models.signals import m2m_changed, post_save
from django.dispatch import receiver
from django.core.files.images import ImageFile

# Own
from vendors.models import Vendor
from utils.normalize import normalize_text
from .utils.models import get_file_name, get_extension

# Third parties
from PIL import Image
import os


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
    num_products = models.PositiveSmallIntegerField("Number of products")
    enable = models.BooleanField("Enable", default=False)

    class Meta:
        verbose_name = "Category"
        verbose_name_plural = "Categories"

    def delete_this_function(self):
        if self.num_products == 0:
            self.enable = False
        else:
            self.enable = True

    def decrease_num_products_field(self):
        self.num_products -= 1

        if self.num_products == 0:
            self.enable = False

        self.save()

    def increase_num_products_field(self):
        self.num_products += 1

        if self.num_products == 0:
            self.enable = True

        self.save()

    def format_category_field(self):
        self.category = self.category.lower().capitalize()

    def pre_save(self):
        self.category = self.category.lower().capitalize()

    def save(self, *args, **kwargs):

        self.pre_save()

        self.delete_this_function()

        super(__class__, self).save(*args, **kwargs)

    def __str__(self):
        return self.category


class Product(models.Model):
    """Prodcut Model"""

    code = models.PositiveSmallIntegerField("Product code")
    name = models.CharField("Name", max_length=50)
    normalized_name = models.CharField("Name", max_length=50, blank=True)
    description = models.TextField("Description",  null=True, blank=True)

    stock = models.SmallIntegerField("Cantidad disponible", null=True)
    in_stock = models.BooleanField("In stock", default=True)
    categories = models.ManyToManyField(Category)
    vendor = models.ForeignKey(Vendor, on_delete=models.CASCADE)
    vendor_code = models.CharField(
        "Vendor code", max_length=25, blank=True, null=True)
    brand = models.ForeignKey(
        Brand, on_delete=models.CASCADE, null=True, blank=True)
    brand_name = models.CharField(
        'Brands', max_length=100, blank=True, null=True)
    price = models.DecimalField("Price", max_digits=7, decimal_places=2)

    img = models.ImageField("Image", upload_to=upload_img, null=True)
    img_small = models.ImageField(
        'Image 270 px',
        upload_to='img/270',
        null=True,
        blank=True
    )
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

    def __add_brand_field(self):

        if self.brand:
            self.brand_name = self.brand.brand.upper()

    def __add_code_field(self):

        list_code = __class__.objects.values_list("code", flat=True)

        reference = max(list_code)

        self.code = reference + 1

    def __add_normalized_name_field(self):

        self.normalized_name = normalize_text(self.name)

    def __pre_delete(self):
        """ Pre delete
        When the instance will be deleted, the number of products related
        to that category decrease
        """
        categories = self.categories.all()

        for category in categories:
            category.decrease_num_products_field()

    def __initial_pre_save(self):
        """ Pre save when the instance will be created """

        self.__add_code_field()
        self.__add_normalized_name_field()
        self.__add_brand_field()

    def __pre_save(self):
        """Pre save when instance was created """

        self.__add_normalized_name_field()
        self.__add_brand_field()

    def delete(self, *args, **kwargs):

        self.__pre_delete()

        super(__class__, self).delete(*args, **kwargs)

    def save(self, *args, **kwargs):

        created = True if self._state.adding else False

        if created:
            self.__initial_pre_save()
        else:
            self.__pre_save()

        super(__class__, self).save(*args, **kwargs)

    def __str__(self):
        return self.name


@receiver(m2m_changed, sender=Product.categories.through)
def change_categories_field(sender, instance, **kwargs):

    categories = instance.categories.all()

    for category in categories:
        if kwargs["action"] == "post_add":
            print('increase')
            category.increase_num_products_field()

        elif kwargs["action"] == "post_remove":
            print('decrease')
            category.decrease_num_products_field()


@receiver(post_save, sender=Product)
def postsave_products(sender, instance, created, **kwargs):

    QUALITY = 75
    FILE_SIZE = 270

    if not created:

        if not instance.img_small:

            file_name = get_file_name(instance.img.name)
            extension = get_extension(instance.img.name)
            temp_path = '.media/img/temp/' + file_name

            original = Image.open(instance.img.path)

            # Resize Image
            width, height = original.size
            r = width / height
            original.thumbnail((FILE_SIZE, int(FILE_SIZE / r)))

            # Save temp
            if extension != '.png':
                original.save(
                    temp_path,
                    optimized=True,
                    quality=QUALITY
                )
            else:
                # .png
                original.save(temp_path)

            temp = open(temp_path, 'rb')

            # Add temp to img_250 field
            instance.img_small = ImageFile(temp)
            instance.img_small.name = file_name
            instance.save()

            temp.close()
            os.remove(temp_path)
