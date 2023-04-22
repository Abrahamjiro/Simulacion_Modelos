import random

cartera = 100
Intentos = 0

def apuesta(cartera, Intentos):
  while cartera>0 or Intentos==100:
    Intentos=Intentos+1
    dado=random.randint(1,6)
    print (Intentos)
    if(dado==1 or dado==3 or dado==5):
      cartera=cartera-100
    elif(dado==2 or dado==4 or dado==6):
      cartera=cartera+200
  print (cartera, Intentos)



apuesta(cartera, Intentos)