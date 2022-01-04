"""
	Write  prices in product images
"""

from PIL import Image, ImageDraw, ImageFont
import os, django

os.environ.setdefault("DJANGO_SETTINGS_MODULE", "dm.settings")
django.setup()

from dm.settings import BASE_DIR
from products.models import Product

PROJECT_PATH = str(BASE_DIR)


def create_directory():
	slash_index = PROJECT_PATH.find("/dm")
	root_path = PROJECT_PATH[0:slash_index]

	directory_path = os.path.join(root_path, "img_with_text")

	if not os.path.exists(directory_path):
		os.mkdir(directory_path)

	return directory_path


def get_file_name(path):
	last_slash = path.rfind("/")
	name = path[last_slash + 1 :]
	return name


def create_img_with_prices():
	products = Product.objects.all()
	font = ImageFont.truetype("Copilme_Light.ttf", 40)
	directory_path = create_directory()

	for p in products:
		# p.img.url[1:] media/img/vendors/file-name.jpg

		imgPath = os.path.join(BASE_DIR, p.img.url[1:])
		img = Image.open(imgPath)
		draw = ImageDraw.Draw(img)
		draw.text((10, 10), "$"+str(p.fixedLowerPrice), font=font, fill="green")
		name = get_file_name(imgPath)
		img.save(os.path.join(directory_path, name))


def Main():

	create_img_with_prices()
	

if __name__ =="__main__":
	Main()
