import os
os.system("clear    ")
edad=19
if edad >= 18:
    print("Felicidades")
    print("eres mayor a 18")
edad=15
if edad > 18:
    print("Felicidades")
    print("eres mayor a 18")
elif edad==18:
    print("tienes 18")
else:
    print("eres menor de edad")

edad=25
tiene_carnet=True
if edad>18 and tiene_carnet:
    print("tiene carnet mayor")
else:
    print("no tiene carnet")