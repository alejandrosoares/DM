# Third parties
from datetime import datetime
import random


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