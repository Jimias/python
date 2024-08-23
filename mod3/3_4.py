vuosiluku = int(input("Anna vuosiluku: "))

if (vuosiluku % 4 == 0 and vuosiluku % 100 != 0) or (vuosiluku % 400 == 0):
    print(str(vuosiluku) + " Tämä vuosi on karkusvuosi")
else:
    print("Vuosiluku ei ole karkausvuosi")
