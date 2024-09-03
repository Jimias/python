import random

def heitä_noppaa():
    return random.randint(1, 6)


while True:
    silmäluku = heitä_noppaa()
    print("Nopan silmäluku" , silmäluku)
    if silmäluku == 6:
        break




