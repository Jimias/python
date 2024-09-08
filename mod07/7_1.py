vuodenajat = (
    ("Talvi" , (12, 1, 2)),
    ("Kevät" , (3, 4, 5)),
    ("Kesä" , (6, 7, 8)),
    ("Talvi" ,  (9, 10, 11))
)

kuukaudenumero = int(input("Anna Kuukaudenumero: "))

for vuodenaika, kuukaudet in vuodenajat:
    if kuukaudenumero in kuukaudet:
        print("Kuukausi" , kuukaudenumero , "kuuluu vuoden aikaan:"  , vuodenaika)
        break



