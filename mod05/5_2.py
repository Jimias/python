lista = []
while True:
    syote = input("Anna luku: ")
    if syote == "":
        break
    luku = int(syote)
    lista.append(luku)

lista.sort(reverse=True)

print(lista[0:5])