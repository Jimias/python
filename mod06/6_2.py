import random

luku_tahko = int(input("Anna Tahkojen määrä: "))

def heitä_noppaa(luku):
    return random.randint(1, luku)


while True:
    silmäluku = heitä_noppaa(luku_tahko)
    print("Nopan silmäluku" , silmäluku)
    if silmäluku == luku_tahko:
        break