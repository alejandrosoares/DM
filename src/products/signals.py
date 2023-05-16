import os
from PIL import Image
from shutil import rmtree

from django.db.models.signals import (
    m2m_changed,
    pre_save,
    post_save,
    pre_delete
)
from django.dispatch import receiver

from utils.normalize import normalize_text
from .models import Product, upload_to
from .utils.models import ImageConvertorFactory


@receiver(m2m_changed, sender=Product.categories.through)
def change_categories_field(sender, instance, **kwargs):

    categories = instance.categories.all()

    for category in categories:
        if kwargs["action"] == "post_add":
            category.increase_num_products()

        elif kwargs["action"] == "post_remove":
            category.decrease_num_products()


@receiver(pre_save, sender=Product)
def pre_save_products(sender, instance, **kwargs):
    def get_product_code():
        list_code = Product.objects.values_list("code", flat=True)
        try:
            ref = max(list_code)
        except ValueError:
            ref = 0
        finally:
            code = ref + 1
            return code

    instance.name = instance.name.upper()
    instance.code = get_product_code()
    instance.normalized_name = normalize_text(instance.name)


@receiver(post_save, sender=Product)
def post_save_products(sender, instance, created, **kwargs):
    def load_webp_img_field(img, upload_path):
        convertor = ImageConvertorFactory.get_convertor(img, upload_path)
        relative_path = convertor.save_webp_image()
        instance.img_webp.name = relative_path

    def load_small_webp_img_field(img, upload_path):
        convertor = ImageConvertorFactory.get_convertor(img, upload_path)
        relative_path = convertor.save_resized_image()
        instance.img_small_webp.name = relative_path

    if instance.optimize_image is False and instance.img:
        upload_path = upload_to(instance.code)
        img = Image.open(instance.img.path)
        load_webp_img_field(img, upload_path)
        load_small_webp_img_field(img, upload_path)

        instance.optimize_image = True
        instance.save()
        img.close()


@receiver(pre_delete, sender=Product)
def pre_delete_products(sender, instance, **kwargs):
    def delete_image_folder():
        image_folder = os.path.dirname(instance.img.path)
        rmtree(image_folder)

    def decrease_number_of_products_of_category():
        categories = instance.categories.all()
        for category in categories:
            category.decrease_num_products()

    delete_image_folder()
    decrease_number_of_products_of_category()