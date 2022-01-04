from django.core.management.base import BaseCommand

import decimal
from products.models import Product




class Command(BaseCommand):


	help = "Change the adjusted price of the products"

	def add_arguments(self, parser):
		parser.add_argument('increase', nargs='+', type=float)



	def handle(self, *args, **options):

		increase = decimal.Decimal(options.get('increase')[0])

		products = Product.objects.all()

		for p in products:
			p.fixedLowerPrice = p.fixedLowerPrice  + increase
			p.fixedHigherPrice = p.fixedHigherPrice  + increase
			p.save()

		print("Cambio de precio finalizado")
