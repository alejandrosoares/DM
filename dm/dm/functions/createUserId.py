'''
	Crea un nuevo userid para luego insertar en las cookies y llevar el seguimiento de las
	actividades del usuario
	Donde se utiliza la funcion: 
		-home.views.HomeView
'''

from user_information.models import UserInformation
from datetime import datetime
import random


def CreateUserId():

	x = True
	date = datetime.today().strftime("%Y%m%d")

	while x:
		randomString = str(random.randint(99999,999999))
		userid = date + randomString
		if  not UserInformation.objects.filter(userid=userid).exists():
			UserInformation.objects.create(userid=userid)
			x = False

	return str(userid)