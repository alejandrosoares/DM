from django.db import models

# Para user juntos con las views.

class UserInformation(models.Model):
	# Se puede generar un usuario anonimo donde se registre todas las visualizaciones de los productos
	# userid de usuario anonimo 2020251100000
	userid = models.CharField(verbose_name="ID de usuario", max_length=20)

	def __str__(self):
		return self.userid
