# class Mahasiswa:
#     def __init__(self, nim, nama, ipk):
#         self.nim = nim
#         self.nama = nama
#         self.__ipk = ipk

#     @property
#     def ipk(self):
#         return self.__ipk

#     @ipk.setter
#     def ipk(self, value):
#         if 0.0 <= value <= 4.0:
#             self.__ipk = value
#         else:
#             raise ValueError("IPK harus 0.0 sampai 4.0")        

# class MahasiswaS1(Mahasiswa):
#     def __init__(self, nim, nama, ipk, judul_skripsi):
#         super().__init__(nim, nama, ipk)
#         self.judul_skripsi = judul_skripsi

#     def info_skripsi(self):
#         # print(f"Skripsi: {self.judul_skripsi}")
#         return f"Skripsi: {self.judul_skripsi}"

#     def predikat(self):
#         return "Cumlaude" if self.ipk >= 3.5 else "Tidak cumlaude"

# class MahasiswaS2(Mahasiswa):
#     def __init__(self, nim, nama, ipk, judul_skripsi):
#         super().__init__(nim, nama, ipk)
#         self.judul_skripsi = judul_skripsi

#     def info_skripsi(self):
#         # print(f"Skripsi: {self.judul_skripsi}")
#         return f"Skripsi: {self.judul_skripsi}"

#     def predikat(self):
#         return "Cumlaude" if self.ipk >= 3.75 else "Tidak cumlaude"
        
# m1 = Mahasiswa("E42027512", "Rani", 3.7)
# # m2 = MahasiswaS1("E41210002", "Budi", 3.6, "Sistem Pakar")
# # daftar = [m2, MahasiswaS2("E41210003","Sari",3.8,"Tesis AI")]

# m1.ipk             = 5.0 
# # m2.ipk = 3.3

# print(m1._Mahasiswa__ipk)

# for mhs in daftar:
#     print(mhs.nama, "->", mhs.predikat())

# m2.info_skripsi()
# print(m2.info_skripsi())
# print(m2.ipk, m2.nama)






from abc import ABC, abstractmethod

class Mahasiswa(ABC):
    def __ini__(self, nim, nama, ipk):
        self.nim = nim
        self.nama = nama
        self.ipk =ipk
        # self.nim, nama, ipk = nim, nama, ipk

