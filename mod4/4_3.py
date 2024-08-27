lista = []
while True:
    syote = input("Anna luku: ")
    if syote == "":
        break
    luku = int(syote)
    lista.append(luku)

pienin = min(lista)
suurin = max(lista)

print("pienin luku on: ", pienin , "suurin luku on: ", suurin)
