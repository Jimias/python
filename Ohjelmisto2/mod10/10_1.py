class Hissi:
    def __init__(self, alinkerrosnmr, ylinkerrosnmr):
        self.alinkerros = alinkerrosnmr
        self.ylinkerros = ylinkerrosnmr
        self.nyky_kerros = alinkerrosnmr

    def siirry_kerrokseen(self, kerros):

        while self.nyky_kerros != kerros:
            if self.nyky_kerros < kerros:
                self.kerros_ylös()
            else:
                self.kerros_alas()



    def kerros_ylös(self):
        if self.nyky_kerros < self.ylinkerros:
            self.nyky_kerros += 1
            print(f"Hissi siirtyi kerrokseen {self.nyky_kerros}.")
        else:
            print("Hissi on jo ylimmässä kerroksessa.")




    def kerros_alas(self):
        if self.nyky_kerros > self.alinkerros:
            self.nyky_kerros -= 1
            print(f"Hissi siirtyi kerrokseen {self.nyky_kerros}.")
        else:
            print("Hissi on jo alimmassa kerroksessa.")


if __name__ == "__main__":
    h = Hissi(1, 10)

    h.siirry_kerrokseen(5)

    h.siirry_kerrokseen(1)

