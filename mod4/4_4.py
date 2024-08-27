import random

oikealuku = random.randint(1, 10)

print("Arvaa luku 1-10 väliltä")

while True:
    arvaus = int(input("Anna arvaus: "))
    if arvaus > oikealuku:
        print("Luku on pienempi")
    elif arvaus < oikealuku:
        print("luku on suurempi")
    else:
        print("luku on oikea")
        break


