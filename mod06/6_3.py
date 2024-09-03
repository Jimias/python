def bensamaara(polttoaine):
    return polttoaine * 3.785


#paaohjelma
polttoaine = int(input("Anna bensan määrä galloonissa: "))

while True:
    if polttoaine <= 0:
        break
    litrat = bensamaara(polttoaine)
    print("Gallooni määrä minkä syötit on litroissa: ", litrat)

    polttoaine = int(input("Anna bensan määrä galloonissa: "))

