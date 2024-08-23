eka_str = input("Anna Leiviskät: ")
toka_str= input("Anna Naulat: ")
kolmas_str = input("Anna Luodit: ")
eka = float(eka_str)
toka = float(toka_str)
kolmas = float(kolmas_str)
naulat = eka * 20
luodit = (toka + naulat) * 32
paino = (kolmas + luodit) * 13.3

kilo = int(paino // 1000)
gramma = float(paino % 1000)

print("Massa nykymittojen mukaan: " + str(kilo) +" kilogrammaa " + f"{gramma:.2f} grammaa")
