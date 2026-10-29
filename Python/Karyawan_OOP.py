from abc import ABC, abstractmethod

class Karyawan(ABC):
    def __init__(self, id_karyawan, nama, gaji_pokok):
        self.id_karyawan = id_karyawan
        self.nama = nama
        self.__gaji_pokok = gaji_pokok

    @property
    def gaji_pokok(self):
        return self.__gaji_pokok

    @gaji_pokok.setter
    def gaji_pokok(self, value):
        if value > 0:
            self.__gaji_pokok = value
        else:
            raise ValueError("Gaji pokok tidak boleh negatif")

    @abstractmethod
    def hitung_gaji(self):
        pass

class KaryawanTetap(Karyawan):
    def __init__(self, id_karyawan, nama, gaji_pokok):
        super().__init__(id_karyawan, nama, gaji_pokok)

    def hitung_gaji(self):
        gaji_total = self.gaji_pokok * 1.2 
        return (f"Gaji total adalah: Rp {gaji_total:,.0f}") 

class KaryawanKontrak(Karyawan):
    def __init__(self, id_karyawan, nama, gaji_pokok):
        super().__init__(id_karyawan, nama, gaji_pokok)

    def hitung_gaji(self):
        gaji_total = self.gaji_pokok + 300000
        return (f"Gaji total adalah: Rp {gaji_total:,.0f}")


k1 = KaryawanTetap("KT001", "Andi", 2500000.0)
k2 = KaryawanKontrak("KK001", "Bulan", 1500000.0)

k1.gaji_pokok = 1000000

# print(f"Gaji pokok: Rp {k1._Karyawan__gaji_pokok:,.0f}")
# print(f"Gaji pokok: Rp {k2._Karyawan__gaji_pokok:,.0f}")
print(f"Gaji pokok: Rp {k1.gaji_pokok:,.0f}")
print(f"Gaji pokok: Rp {k2.gaji_pokok:,.0f}")
print()
print(k1.hitung_gaji())
print(k2.hitung_gaji())