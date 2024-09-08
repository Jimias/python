nimet = set()

while True:
    nimi = str(input("Anna nimi: "))
    if nimi == "":
        break
    if nimi in nimet:
        print("aiemmin syötetty")
    else:
        print("uusi nimi")
    nimet.add(nimi)

for nimi in nimet:
    print(nimi)