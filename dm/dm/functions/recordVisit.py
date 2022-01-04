'''
	Funcion que registra las fechas de las visitas del usuario a la pagina
	Los registros se crean por:
		Acceso a la pagina mediante el navegador
		Acceso a la pagina por medio de una publicacion
'''
from user_information.models import UserInformation, DateOfVisit

def RecordVisit(userid, lastPage, browser, versionBrowser):
	try:
		user = UserInformation.objects.get(userid=userid)
		DateOfVisit.objects.create(user=user, lastPage=lastPage, browser=browser, versionBrowser=versionBrowser)
	except UserInformation.DoesNotExist:
		print(f"El {userid} no existe en la base de datos")
