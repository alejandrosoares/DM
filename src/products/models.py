import os

from django.db import models


def upload_to(product_code: int) -> str:
    code = str(product_code)
    upload_path = os.path.join('img', 'products', f'{code}/')
    return upload_path


def upload_img_product(instance, filename):
    product_code = instance.code
    upload_path = upload_to(product_code)
    return os.path.join(upload_path, filename)


class Brand(models.Model):

    name = models.CharField(max_length=50)

    def save(self, *args, **kwargs):
        self.name = self.name.upper()
        super(__class__, self).save(*args, **kwargs)

    def __str__(self):
        return self.name


class Category(models.Model):

    name = models.CharField(max_length=30)
    num_products = models.PositiveSmallIntegerField("Number of products")
    enable = models.BooleanField(default=False)

    class Meta:
        indexes = [
            models.Index(fields=['enable'], name='category_enable_idx')
        ]

    def decrease_num_products(self):
        self.num_products -= 1
        if self.num_products == 0:
            self.enable = False
        self.save()

    def increase_num_products(self):
        self.num_products += 1
        if self.num_products == 0:
            self.enable = True
        self.save()

    def save(self, *args, **kwargs):
        self.name = self.name.lower().capitalize()
        super(__class__, self).save(*args, **kwargs)

    def __str__(self):
        return self.name


class Product(models.Model):

    categories = models.ManyToManyField(Category, related_name='products')
    brand = models.ForeignKey(Brand, on_delete=models.CASCADE,
                              null=True, blank=True)

    code = models.PositiveSmallIntegerField()
    name = models.CharField(max_length=50)
    normalized_name = models.CharField(max_length=50, blank=True)
    description = models.TextField(null=True, blank=True)
    stock = models.SmallIntegerField(null=True)
    in_stock = models.BooleanField(default=True)
    price = models.DecimalField(max_digits=7, decimal_places=2)

    img = models.ImageField(upload_to=upload_img_product, null=True)
    img_webp = models.ImageField(null=True, blank=True)
    img_small_webp = models.ImageField(null=True, blank=True)
    optimize_image = models.BooleanField(default=False)

    class Meta:
        indexes = [
            models.Index(fields=['code'], name='product_code_idx')
        ]

    def __str__(self):
        return self.name
