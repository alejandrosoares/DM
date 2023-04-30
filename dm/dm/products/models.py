# Django
from django.db import models
from django.db.models.signals import m2m_changed, post_save, pre_delete
from django.dispatch import receiver
from django.core.files.images import ImageFile

# Own
from utils.normalize import normalize_text
from .utils.models import (
    get_file_name,
    get_small_filename,
    replace_extension_to_webp,
    get_path
)

# Third parties
from PIL import Image
import os
from shutil import rmtree


def upload_img(instance, filename):
    """For delete, but conflict in migrations"""
    return upload_img_product(instance, filename)


def upload_img_webp(instance, filename):
    """For delete, but conflict in migrations"""
    return upload_img_product(instance, filename)


def upload_img_product(instance, filename):

    return f'img/products/{instance.code}/{filename}'


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
    brand = models.ForeignKey(
        Brand, on_delete=models.CASCADE, null=True, blank=True)
    brand_name = models.CharField(
        "Brands", max_length=100, blank=True, null=True)
    price = models.DecimalField("Price", max_digits=7, decimal_places=2)

    img = models.ImageField("Image", upload_to=upload_img_product, null=True)
    img_small = models.ImageField(
        "Small version",
        upload_to=upload_img_product,
        null=True,
        blank=True
    )
    img_webp = models.ImageField(
        "Original webp",
        upload_to=upload_img_product,
        null=True,
        blank=True
    )
    img_small_webp = models.ImageField(
        "Small webp",
        upload_to=upload_img_product,
        null=True,
        blank=True
    )

    load_img = models.BooleanField("Load img", default=False)

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
            return '{} | {}'.format(
                self.name,
                self.brand
            )
        else:
            return self.name

    def __to_uppercase_name_field(self):

        self.name = self.name.upper()

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

        self.__to_uppercase_name_field()
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
            category.increase_num_products_field()

        elif kwargs["action"] == "post_remove":
            category.decrease_num_products_field()


@receiver(post_save, sender=Product)
def postsave_products(sender, instance, created, **kwargs):
    """ Post Save Products

    Generate img and load in fields

    Files:
    1-ORIGINAL
    2-ORIGINAL WEBP (generated in temp folder)
    3-RESIZE (generated in temp folder)
    4-RESIZE WEBP (generated in temp folder)

    Operations:
    - Save temporal:
    - Load the file from temp folder and load in  model field 
    """

    FILE_SIZE = 270
    TEMP_FOLDER = '.media/img/temp/'

    if instance.load_img is False:

        filename = get_file_name(instance.img.name)

        img = Image.open(instance.img.path)

        ##################################################################
        # Save 2 ORIGINAL WEBP
        original_webp_name = replace_extension_to_webp(filename)
        img.save(TEMP_FOLDER + original_webp_name, format='webp')

        # Load 2 ORIGINAL WEBP
        original_webp = open(TEMP_FOLDER + original_webp_name, mode='rb')
        instance.img_webp = ImageFile(original_webp)
        instance.img_webp.name = original_webp_name

        os.remove(TEMP_FOLDER + original_webp_name)

        ##################################################################
        # Save 3 RESIZE
        width, height = img.size
        r = width / height
        img.thumbnail((FILE_SIZE, int(FILE_SIZE / r)))
        resize_name = get_small_filename(filename)
        img.save(TEMP_FOLDER + resize_name)

        # Load 3 RESIZE
        resize = open(TEMP_FOLDER + resize_name, 'rb')
        instance.img_small = ImageFile(resize)
        instance.img_small.name = resize_name

        os.remove(TEMP_FOLDER + resize_name)

        ##################################################################
        # Save 4 RESIZE WEBP
        resize_name_webp = replace_extension_to_webp(resize_name)
        img.save(TEMP_FOLDER + resize_name_webp, format='webp')

        # Load 4 RESIZE WEBP
        resize_webp = open(TEMP_FOLDER + resize_name_webp, 'rb')
        instance.img_small_webp = ImageFile(resize_webp)
        instance.img_small_webp.name = resize_name_webp

        os.remove(TEMP_FOLDER + resize_name_webp)

        ##################################################################
        # Save instance
        instance.load_img = True
        instance.save()

        # Close files
        original_webp.close()
        resize.close()
        resize_webp.close()
        img.close()


@receiver(pre_delete, sender=Product)
def predelete_products(sender, instance, **kwargs):
    """Pre delete products
    Delete folder of images of the instance
    """
    path = get_path(instance.img_webp.path)

    rmtree(path)
