from rest_framework import serializers

from products.models import Product


class ProductListSerializer(serializers.ModelSerializer):
    img = serializers.SerializerMethodField()

    class Meta:
        model = Product
        fields = ['id', 'name', 'price', 'img']

    def get_img(self, obj):
        return {
            'url': obj.img_small_webp.url,
            'width': obj.img_small_webp.width,
            'height': obj.img_small_webp.height
        }
