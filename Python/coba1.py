"""Contoh reservasi ruang dengan tiga class utama.

Relasi dan multiplicity:
- Mahasiswa 1 -- 0..* Reservasi: satu mahasiswa dapat memiliki banyak
  reservasi; setiap reservasi terkait tepat dengan satu mahasiswa.
- Ruang 1 -- 0..* Reservasi: satu ruang dapat memiliki banyak reservasi
  pada tanggal yang berbeda; setiap reservasi memakai tepat satu ruang.

Contoh ini menganggap satu ruang hanya dapat dipesan satu kali pada tanggal
yang sama. Enkapsulasi menggunakan atribut privat; abstraksi ditunjukkan oleh
method publik yang menyembunyikan cara pengecekan dan penyimpanan reservasi.
Pewarisan dan polimorfisme tidak dipaksakan karena model ini hanya memiliki
satu jenis mahasiswa, reservasi, dan ruang.
"""

from __future__ import annotations

from datetime import date


class Mahasiswa:
    def __init__(self, nim: str, password: str) -> None:
        self.__nim = nim
        self.__password = password
        self.__reservasi: list[Reservasi] = []

    @property
    def nim(self) -> str:
        return self.__nim

    @property
    def reservasi(self) -> tuple[Reservasi, ...]:
        return tuple(self.__reservasi)

    def login(self, nim: str, password: str) -> bool:
        """Memeriksa NIM dan password mahasiswa."""
        return nim == self.__nim and password == self.__password

    def _catat_reservasi(self, reservasi: Reservasi) -> None:
        self.__reservasi.append(reservasi)


class Ruang:
    def __init__(self, koderuang: str) -> None:
        self.__koderuang = koderuang
        self.__reservasi: list[Reservasi] = []

    @property
    def koderuang(self) -> str:
        return self.__koderuang

    @property
    def reservasi(self) -> tuple[Reservasi, ...]:
        return tuple(self.__reservasi)

    def cektersedia(self, tanggal: date) -> bool:
        """Mengembalikan True jika ruang belum dipesan pada tanggal itu."""
        return all(pesan.tanggal != tanggal for pesan in self.__reservasi)

    def _catat_reservasi(self, reservasi: Reservasi) -> None:
        self.__reservasi.append(reservasi)


class Reservasi:
    def __init__(self, tanggal: date, mahasiswa: Mahasiswa, ruang: Ruang,) -> None:
        self.__tanggal = tanggal
        self.__mahasiswa = mahasiswa
        self.__ruang = ruang
        self.__dibuat = False

    @property
    def tanggal(self) -> date:
        return self.__tanggal

    @property
    def mahasiswa(self) -> Mahasiswa:
        return self.__mahasiswa

    @property
    def ruang(self) -> Ruang:
        return self.__ruang

    def buatreservasi(self) -> bool:
        """Buat reservasi jika ruang tersedia; False jika sudah dipesan."""
        if self.__dibuat or not self.__ruang.cektersedia(self.__tanggal):
            return False

        self.__ruang._catat_reservasi(self)
        self.__mahasiswa._catat_reservasi(self)
        self.__dibuat = True
        return True


if __name__ == "__main__":
    mahasiswa = Mahasiswa("12345", "pw123")
    ruang = Ruang("R101")
    tanggal_pesan = date.today()

    if mahasiswa.login("12345", "pw123"):
        print("Login berhasil.")
        reservasi = Reservasi(tanggal_pesan, mahasiswa, ruang)
        if reservasi.buatreservasi():
            print(f"Reservasi {ruang.koderuang} tanggal {tanggal_pesan} berhasil.")
        else:
            print("Ruang sudah dipesan pada tanggal tersebut.")
    else:
        print("Login gagal.")
