# Own
from user_information.models import UserInformation

# Third parties
from datetime import datetime
import random


def create_userid_for_cookies():
   """Create userid for insert in the cookies
   Track user activities
   @return: str
   """

   date = datetime.today().strftime("%Y%m%d")

   while True:

      userid = date + str(random.randint(9999, 999999))
      
      if  not UserInformation.objects.filter(userid=userid).exists():
         UserInformation.objects.create(userid=userid)
         break

   return userid





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


'''
	Redondea los precio segun los siguiente criterios:
	# 82.5 llevarlo a 85
	# 108 llevarlo a 110

'''
def RoundPrice(auxiliary):
   x = True # indica que llega a la unidad
   unitOfThousand = 0
   unitOfHundred = 0
   unitTen = 0

   while x:
      if auxiliary/1000 > 1:
         unitOfThousand = auxiliary//1000
         auxiliary = auxiliary - unitOfThousand * 1000
      else:
         if auxiliary/100 > 1:
            unitOfHundred = auxiliary//100
            auxiliary = auxiliary - unitOfHundred * 100
         else:
            if auxiliary/10 > 1:
               unitTen = auxiliary//10
               auxiliary = auxiliary - unitTen * 10
               
            else:
               x = False
               if auxiliary  < 5:
                  auxiliary = 5
               elif auxiliary > 5:
                  auxiliary = 0
                  unitTen += 1
                  if unitTen == 10:
                     # Era 9 y al incrementar paso a ser 10 y por lo tanto tengo que sumar en unitOfHundred a uno
                     unitTen = 0
                     unitOfHundred += 1

                     if unitOfHundred == 10:
                        unitOfHundred = 0
                        unitOfThousand += 1


   finalValue = unitOfThousand *1000 + unitOfHundred * 100 + unitTen * 10 + auxiliary

   return finalValue