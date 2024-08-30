kaupunkilista = []

kaupungit = 0
maxkaupungit = 5

print("Anna viiden eri kaupungin nimi")

kaupunki = input("Anna kaupunki: ")
kaupunkilista.append(kaupunki)

while (kaupunki != "") and kaupungit < maxkaupungit -1:
    kaupungit +=1
    kaupunki = input("Anna kaupunki: ")
    kaupunkilista.append(kaupunki)

for kaupunki in kaupunkilista:
    print(kaupunki)

