import math
import random
numero =[]

arpakuutio = int(input("Anna arpakuutioiden lukumäärä: "))

for _ in range(arpakuutio):
    numero.append(random.randint(1 , 6))
    summa = sum(numero)
print("Arpakuutioiden yhteisumma on: " , summa)