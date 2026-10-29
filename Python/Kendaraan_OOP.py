from abc import ABC, abstractmethod

class Kendaraan(ABC):
    def __init__(self, tarif_dasar = float, plat_nomor = str):
        self.tarif_dasar = tarif_dasar
        self.__plat_nomor = plat_nomor

    @property
    def plat_nomor(self):
        return self.__plat_nomor

    @abstractmethod
    def hitung_biaya_sewa(self, lama_hari):
        pass 

class Motor(Kendaraan):
    def __init__(self, tarif_dasar, plat_nomor, jenis):
        super().__init__(tarif_dasar, plat_nomor)
        self.jenis = jenis

    def hitung_biaya_sewa(self, lama_hari):
        return self.tarif_dasar * lama_hari

class Mobil(Kendaraan):
    def __init__(self, tarif_dasar, plat_nomor, jenis):
        super().__init__(tarif_dasar, plat_nomor)
        self.jenis = jenis

    def hitung_biaya_sewa(self,lama_hari):
        return self.tarif_dasar * lama_hari + 50000

motor1 = Motor(30000, "B1234XYZ", "Motor")
mobil1 = Mobil(120000, "B5678ABC", "Mobil")

list = [motor1, mobil1]

lama_hari = 3

print(f"Biaya untuk parkir selama {lama_hari} hari adalah")
for m in list:
    biaya = m.hitung_biaya_sewa(lama_hari)
    print(f"{m.plat_nomor} - {m.jenis} -> Rp {m.hitung_biaya_sewa(lama_hari):,.0f}")