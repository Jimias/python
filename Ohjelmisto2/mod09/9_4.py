import random

class Auto:
    def __init__(self, rekkari, huippunopeus):
        self.rekisteritunnus =rekkari
        self.huippunopeus = huippunopeus
        self.nopeus = 0
        self.matka = 0

    def kiihdyta(self, nopeudenmuutos):
        self.nopeus += nopeudenmuutos

        if self.nopeus < 0:
            self.nopeus = 0
        elif self.nopeus > self.huippunopeus:
            self.nopeus = self.huippunopeus


    def kulje(self, tuntimaara):
        self.matka += self.nopeus * tuntimaara


if __name__ == "__main__":
    autot = []

    for i in range(1, 11):
        rekkari = f"ABC-{i}"
        huippunopeus = random.randint(100, 200)
        autot.append(Auto(rekkari, huippunopeus))

    kilpailu = True
    while kilpailu:
        for auto in autot:
            nopeudenmuutos = random.randint(-10, 15)
            auto.kiihdyta(nopeudenmuutos)

            auto.kulje(1)

            if auto.matka >= 10000:
                kilpailu = False
                break
    print(f"{'Rekisteritunnus':<15}{'Huippunopeus (km/h)':<20}{'Nykyinen nopeus (km/h)':<25}{'Kuljettu matka (km)':<20}")
    print("-" * 80)
    for auto in autot:
        print(f"{auto.rekisteritunnus:<15}{auto.huippunopeus:<20}{auto.nopeus:<25}{auto.matka:<20.2f}")