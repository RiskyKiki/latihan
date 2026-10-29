class Calc:
    def __init__(self, angka1, angka2):
        self.angka1 = angka1
        self.angka2 = angka2

    def perkalian(self):
        hasil = self.angka1 * self.angka2
        print(f"{self.angka1} x {self.angka2} = {hasil}")
    def pembagian(self):
        hasil = self.angka1 / self.angka2
        print(f"{self.angka1} : {self.angka2} = {hasil}")
    def penjumlahan(self):
        hasil = self.angka1 + self.angka2
        print(f"{self.angka1} + {self.angka2} = {hasil}")
    def pengurangan(self):
        hasil = self.angka1 - self.angka2
        print(f"{self.angka1} - {self.angka2} = {hasil}")

angka = Calc(5,2)
# angka = Calc(int(input("Angka pertama ")), int(input("Angka kedua ")))

angka.penjumlahan()
angka.pengurangan()
angka.perkalian()
angka.pembagian()




