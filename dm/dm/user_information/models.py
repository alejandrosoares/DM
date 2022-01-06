# Django
from django.db import models
from django.db.models.signals import post_save
from django.dispatch import receiver

# Own
from products.models import Category, Product, Brand


class Queries(models.Model):
	#	Registra las consultas que se realizan el la barra de busqueda
	query = models.CharField(verbose_name="Consulta realizada", max_length=50)

	class Meta:
		verbose_name = "Consulta"
		verbose_name_plural = "Consultas"

class UseOfCategories(models.Model):
	category = models.OneToOneField(Category, on_delete=models.CASCADE)
	quantity = models.PositiveIntegerField(verbose_name="Cantidad de consultas", default=0)

	class Meta:
		verbose_name = "Uso de categoria"
		verbose_name_plural = "Uso de categorias"
		ordering = ['-quantity']

	@property
	def Categoria(self):
		return '{}'.format(self.category.category)

	def __str__(self):
		return self.Categoria

class SearchWords(models.Model):
	#	Modelo para guardar las busquedas realizadas, mediante la cuadro de resultado de coincidentes
	#	Presenta la lista de items coincidente con los que se escribe y cuando se hace click(para buscar el articulo)
	#	se registra que se busco el articulos
	string = models.CharField(verbose_name="Texto", max_length=50)
	typeString = models.CharField(verbose_name="Tipo de texto", max_length=1)
	idObject = models.IntegerField(verbose_name="Id de object")
	img = models.ImageField(verbose_name="Imagen", upload_to='img/', null=True, blank=True)
	quantity = models.PositiveIntegerField(verbose_name="Contador de cantidades de consultas", default=0)
	priority = models.BooleanField(verbose_name="Prioridad", default=False)

	class Meta:
		verbose_name = "Item consultado"
		verbose_name_plural = "Items consultados"
		ordering = ['-priority','-quantity']


class ProductsOfInterest(models.Model):
	#	Registra los productos que a mirado el usuario

	idProduct = models.PositiveIntegerField(verbose_name="Id de producto de interes")
	quantity = models.PositiveIntegerField(verbose_name="Cantidad de visualizaciones")
	date = models.DateField(verbose_name="Fecha de registro", auto_now_add=True, auto_now=False)

	@property
	def User(self):
		return "{}".format(self.user.userid)

	def __str__(self):
		return self.User

class DateOfVisit(models.Model):
	#	Solo para usuarios que los pueda identificar
	#	Registra las visitas de los usuarios
	date = models.DateField(verbose_name="Fecha visita", auto_now_add=True, auto_now=False)
	lastPage = models.URLField(verbose_name="Pagina de la que proviene", null=True)
	browser = models.CharField(verbose_name="Navegador", max_length=20, null=True)
	versionBrowser = models.CharField(verbose_name="Version del Navegador", max_length=5, null=True)

	@property
	def User(self):
		return "{}".format(self.user.userid)

	def __str__(self):
		return self.User


@receiver(post_save, sender=Brand)
def PostSaveBrand(sender, instance, created, **kwargs):
	if created:
		SearchWords.objects.create(string=instance.brandName, typeString='b', idObject=instance.id, img=None, priority=True)

@receiver(post_save, sender=Product)
def PostSaveProducto(sender, instance, created, **kwargs):
	if created:
		if instance.brand:
			name = instance.name + " (" + instance.brand.brand + ")"
		else:
			name = instance.name
		SearchWords.objects.create(string=name, typeString='p', idObject=instance.id, img=instance.img, priority=False)

@receiver(post_save, sender=Category)
def PostSaveCategory(sender, instance, created, **kwargs):
	if created:
		UseOfCategories.objects.create(category=instance)