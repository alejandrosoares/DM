'''
	Formatea  el string con los productos visualizados que viene desde la template home.html 
	los convierte en una lista y los guarda
	Donde se utiliza la funcion:
		-home.views.ReceivingData
'''
from user_information.models import ProductsOfInterest

def RecordMaker(string, userinfo):
	string = string.replace("[","").replace("]", "")
	listString = string.split(",")

	try:
		if len(listString) % 2 == 0: # La cant de datos son pares
			for x in range(len(listString) - 1):
				if x % 2 == 0 or x == 0:
					ProductsOfInterest.objects.create(user=userinfo, idProduct=listString[x], quantity=listString[x + 1])
	except:
		print("Hubo un error en la lista de datos listCodes")		