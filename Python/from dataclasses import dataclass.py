from dataclasses import dataclass
from datetime import datetime, timedelta
from typing import Dict, List, Optional


# BAGIAN 1: KELAS DATA
@dataclass
class Mahasiswa:
    nim: str
    password: str


@dataclass
class Ruang:
    kode: str
    gedung: str
    kapasitas: int


@dataclass
class Reservasi:
    id: int
    nim: str
    kode_ruang: str
    mulai: datetime
    selesai: datetime
    status: str = "disetujui"


# BAGIAN 2: LAYANAN SISTEM RESERVASI
class SistemReservasi:
    def __init__(self) -> None:
        # Dictionary dipakai sebagai penyimpanan sementara di memori.
        self.mahasiswa: Dict[str, Mahasiswa] = {}
        self.ruang: Dict[str, Ruang] = {}
        self.reservasi: Dict[int, Reservasi] = {}

        self.mahasiswa_login: Optional[Mahasiswa] = None
        self._id_reservasi = 1

    def tambah_mahasiswa(self, mahasiswa: Mahasiswa) -> None:
        self.mahasiswa[mahasiswa.nim] = mahasiswa

    def login(self, nim: str, password: str) -> bool:
        mahasiswa = self.mahasiswa.get(nim)

        if mahasiswa is None or mahasiswa.password != password:
            return False

        self.mahasiswa_login = mahasiswa
        return True

    def logout(self) -> None:
        self.mahasiswa_login = None

    @staticmethod
    def _validasi_waktu(mulai: datetime, selesai: datetime) -> None:
        if mulai >= selesai:
            raise ValueError("Waktu selesai harus setelah waktu mulai.")

    @staticmethod
    def _bertabrakan(
        mulai: datetime,
        selesai: datetime,
        reservasi: Reservasi
    ) -> bool:
        return (
            reservasi.status == "disetujui"
            and mulai < reservasi.selesai
            and reservasi.mulai < selesai
        )

    def cari_ruang(
        self,
        gedung: Optional[str] = None,
        kapasitas_min: int = 1,
        mulai: Optional[datetime] = None,
        selesai: Optional[datetime] = None
    ) -> List[Ruang]:
        if (mulai is None) != (selesai is None):
            raise ValueError(
                "Waktu mulai dan selesai harus diisi bersama."
            )

        if mulai is not None and selesai is not None:
            self._validasi_waktu(mulai, selesai)

        hasil = []

        for ruang in self.ruang.values():
            if gedung is not None and ruang.gedung.lower() != gedung.lower():
                continue

            if ruang.kapasitas < kapasitas_min:
                continue

            if mulai is not None and selesai is not None:
                tersedia = all(
                    not self._bertabrakan(mulai, selesai, reservasi)
                    for reservasi in self.reservasi.values()
                    if reservasi.kode_ruang == ruang.kode
                )

                if not tersedia:
                    continue

            hasil.append(ruang)

        return hasil

    def buat_reservasi(
        self,
        kode_ruang: str,
        mulai: datetime,
        selesai: datetime
    ) -> Reservasi:
        if self.mahasiswa_login is None:
            raise PermissionError("Login terlebih dahulu sebagai mahasiswa.")

        self._validasi_waktu(mulai, selesai)

        if kode_ruang not in self.ruang:
            raise ValueError("Kode ruang tidak ditemukan.")

        bentrok = any(
            reservasi.kode_ruang == kode_ruang
            and self._bertabrakan(mulai, selesai, reservasi)
            for reservasi in self.reservasi.values()
        )

        if bentrok:
            raise ValueError("Ruang sudah dipesan pada waktu tersebut.")

        reservasi = Reservasi(
            id=self._id_reservasi,
            nim=self.mahasiswa_login.nim,
            kode_ruang=kode_ruang,
            mulai=mulai,
            selesai=selesai,
        )

        self.reservasi[reservasi.id] = reservasi
        self._id_reservasi += 1
        return reservasi

    def batalkan_reservasi(
        self,
        id_reservasi: int,
        waktu_sekarang: Optional[datetime] = None
    ) -> None:
        if self.mahasiswa_login is None:
            raise PermissionError("Login terlebih dahulu sebagai mahasiswa.")

        reservasi = self.reservasi.get(id_reservasi)

        if reservasi is None or reservasi.nim != self.mahasiswa_login.nim:
            raise ValueError(
                "Reservasi tidak ditemukan atau bukan milik Anda."
            )

        if reservasi.status != "disetujui":
            raise ValueError("Reservasi sudah tidak aktif.")

        sekarang = waktu_sekarang or datetime.now()
        batas_pembatalan = reservasi.mulai - timedelta(hours=2)

        if sekarang > batas_pembatalan:
            raise ValueError(
                "Pembatalan hanya boleh paling lambat 2 jam sebelumnya."
            )

        reservasi.status = "dibatalkan"


# BAGIAN 3: FITUR ADMIN FASILITAS
class AdminFasilitas:
    def __init__(self, sistem: SistemReservasi) -> None:
        self.sistem = sistem

    def tambah_ruang(self, ruang: Ruang) -> None:
        if ruang.kode in self.sistem.ruang:
            raise ValueError("Kode ruang sudah digunakan.")

        self.sistem.ruang[ruang.kode] = ruang

    def ubah_ruang(
        self,
        kode: str,
        gedung: str,
        kapasitas: int
    ) -> None:
        ruang = self.sistem.ruang.get(kode)

        if ruang is None:
            raise ValueError("Ruang tidak ditemukan.")

        ruang.gedung = gedung
        ruang.kapasitas = kapasitas

    def hapus_ruang(self, kode: str) -> None:
        if kode not in self.sistem.ruang:
            raise ValueError("Ruang tidak ditemukan.")

        masih_dipesan = any(
            reservasi.kode_ruang == kode
            and reservasi.status == "disetujui"
            for reservasi in self.sistem.reservasi.values()
        )

        if masih_dipesan:
            raise ValueError("Ruang masih memiliki reservasi aktif.")

        del self.sistem.ruang[kode]

    def laporan_penggunaan(
        self,
        dari: datetime,
        sampai: datetime
    ) -> List[Reservasi]:
        if dari > sampai:
            raise ValueError(
                "Tanggal awal tidak boleh setelah tanggal akhir."
            )

        return [
            reservasi
            for reservasi in self.sistem.reservasi.values()
            if reservasi.status == "disetujui"
            and reservasi.mulai <= sampai
            and reservasi.selesai >= dari
        ]


# BAGIAN 4: CONTOH PEMAKAIAN
def contoh_penggunaan() -> None:
    sistem = SistemReservasi()
    admin = AdminFasilitas(sistem)

    # Admin menambahkan ruang dan sistem memiliki data mahasiswa contoh.
    admin.tambah_ruang(Ruang("R101", "Gedung A", 20))
    sistem.tambah_mahasiswa(Mahasiswa("23001", "rahasia"))

    if sistem.login("23001", "rahasia"):
        mulai = datetime.now() + timedelta(days=1)
        selesai = mulai + timedelta(hours=2)

        pilihan = sistem.cari_ruang(
            gedung="Gedung A",
            kapasitas_min=10,
            mulai=mulai,
            selesai=selesai,
        )
        print("Ruang tersedia:", pilihan)

        if pilihan:
            reservasi = sistem.buat_reservasi(
                pilihan[0].kode,
                mulai,
                selesai,
            )
            print("Reservasi berhasil:", reservasi)

    sistem.logout()

    laporan = admin.laporan_penggunaan(
        datetime.now(),
        datetime.now() + timedelta(days=7),
    )
    print("Laporan penggunaan:", laporan)


if __name__ == "__main__":
    contoh_penggunaan()