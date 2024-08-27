yritykset = 0

maksimiyritykset = 5

ktunnus = input("Anna käyttäjätunnus: ")
stunnus = input("Anna salasana: ")

while (ktunnus != "python" and stunnus != "rules") and yritykset < maksimiyritykset -1:
    yritykset += 1
    ktunnus = input("Anna käyttäjätunnus: ")
    stunnus = input("Anna salasana: ")

if ktunnus == "python" and stunnus == "rules":
    print("Tervetuloa!")
else:
    print("pääsy evätty")

