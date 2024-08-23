sukupuoli = input("Oletko Mies vai Nainen: ")

if sukupuoli == "Mies":
    hemoglobiini = int(input("Anna hemoglobiiniarvosi: "))
    if 134<=hemoglobiini<195:
        print("hemoglobiini arvosi on normaali")
    elif hemoglobiini>195:
        print("hemoglobiini arvosi on korkea")
    elif hemoglobiini<134:
        print("hemoglobiini arvosi on matala")

if sukupuoli == "Nainen":
    hemoglobiini = int(input("Anna hemoglobiiniarvosi: "))
    if 117<=hemoglobiini<175:
        print("hemoglobiini arvosi on normaali")
    elif hemoglobiini>175:
        print("hemoglobiini arvosi on korkea")
    elif hemoglobiini<117:
        print("hemoglobiini arvosi on matala")
