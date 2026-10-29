from datetime import datetime, timedelta


class Mahasiswa:
    def __init__(self, nim, password):
        self.nim = nim
        self.password = password


class SistemReservasi:
    def __init__(self):
        self.ruang = [
            {"kode": "R101", "gedung": "A", "kapasitas": 20},
            {"kode": "R202", "gedung": "B", "kapasitas": 10},
        ]
        self.reservasi = []
        self.mahasiswa = Mahasiswa("12345", "pw123")

    def cari_ruang(self, gedung, kapasitas, mulai, selesai):
        hasil = []
        for ruang in self.ruang:
            tersedia = True
            for pesan in self.reservasi:
                if (    pesan["kode"] == ruang["kode"]
                    and pesan["status"] == "aktif"
                    and mulai < pesan["selesai"]
                    and pesan["mulai"] < selesai):
                    tersedia = False

            if (        ruang["gedung"] == gedung
                    and ruang["kapasitas"] >= kapasitas
                    and tersedia):
                hasil.append(ruang)
        return hasil

    def buat_reservasi(self, nim, kode, mulai, selesai):
        if mulai >= selesai:
            print("Waktu selesai harus setelah waktu mulai.")
            return

        for pesan in self.reservasi:
            if (        pesan["kode"] == kode 
                    and pesan["status"] == "aktif"
                    and mulai < pesan["selesai"]
                    and pesan["mulai"] < selesai):
                print("Ruang sudah dipesan pada waktu tersebut.")
                return

        for ruang in self.ruang:
            if ruang["kode"] == kode:
                self.reservasi.append({
                    "nim": nim,
                    "kode": kode,
                    "mulai": mulai,
                    "selesai": selesai,
                    "status": "aktif",
                })
                print("Reservasi berhasil.")
                return
        print("Kode ruang tidak ditemukan.")

    def batalkan_reservasi(self, nim, kode):
        for pesan in self.reservasi:
            batas = pesan["mulai"] - timedelta(hours=2)
            if (pesan["nim"] == nim and pesan["kode"] == kode
                    and pesan["status"] == "aktif"):
                if datetime.now() <= batas:
                    pesan["status"] = "dibatalkan"
                    print("Reservasi dibatalkan.")
                else:
                    print("Pembatalan harus dilakukan minimal 2 jam sebelumnya.")
                return
        print("Reservasi tidak ditemukan.")


class AdminFasilitas:
    def __init__(self, sistem):
        self.sistem = sistem

    def kelola_ruang(self):
        aksi = input("Pilih tambah, ubah, atau hapus: ").lower()

        if aksi == "tambah":
            kode = input("Kode ruang: ")
            gedung = input("Gedung: ")
            kapasitas = int(input("Kapasitas: "))
            self.sistem.ruang.append({
                "kode": kode, "gedung": gedung, "kapasitas": kapasitas
            })
            print("Ruang ditambahkan.")

        elif aksi == "ubah":
            kode = input("Kode ruang yang diubah: ")
            for ruang in self.sistem.ruang:
                if ruang["kode"] == kode:
                    ruang["gedung"] = input("Gedung baru: ")
                    ruang["kapasitas"] = int(input("Kapasitas baru: "))
                    print("Ruang diubah.")
                    return
            print("Ruang tidak ditemukan.")

        elif aksi == "hapus":
            kode = input("Kode ruang yang dihapus: ")
            for ruang in self.sistem.ruang:
                if ruang["kode"] == kode:
                    self.sistem.ruang.remove(ruang)
                    print("Ruang dihapus.")
                    return
            print("Ruang tidak ditemukan.")

    def lihat_laporan(self, dari, sampai):
        for pesan in self.sistem.reservasi:
            if (pesan["status"] == "aktif"
                    and pesan["mulai"] <= sampai
                    and pesan["selesai"] >= dari):
                print(pesan["kode"], pesan["mulai"], "-", pesan["selesai"])


def baca_waktu(pesan):
    teks = input(pesan + " (YYYY-MM-DD HH:MM): ")
    return datetime.strptime(teks, "%Y-%m-%d %H:%M")


sistem = SistemReservasi()
admin = AdminFasilitas(sistem)

pilihan = input("Login sebagai mahasiswa atau admin? ").lower()

if pilihan == "mahasiswa":
    nim = input("Masukkan NIM: ")
    password = input("Masukkan password: ")

    if nim == sistem.mahasiswa.nim and password == sistem.mahasiswa.password:
        print("Login berhasil.")
        while True:
            aksi = input("Pilih cari, pesan, batal, atau keluar: ").lower()

            if aksi == "cari" or aksi == "pesan":
                gedung = input("Gedung: ")
                kapasitas = int(input("Kapasitas minimal: "))
                mulai = baca_waktu("Waktu mulai")
                selesai = baca_waktu("Waktu selesai")

                if mulai >= selesai:
                    print("Waktu selesai harus setelah waktu mulai.")
                    continue

                hasil = sistem.cari_ruang(gedung, kapasitas, mulai, selesai)
                print("Ruang tersedia:", hasil)

                if aksi == "pesan" and hasil:
                    sistem.buat_reservasi(
                        nim, hasil[0]["kode"], mulai, selesai
                    )

            elif aksi == "batal":
                kode = input("Kode ruang reservasi: ")
                sistem.batalkan_reservasi(nim, kode)

            elif aksi == "keluar":
                break
    else:
        print("Login gagal.")

elif pilihan == "admin":
    while True:
        aksi = input("Pilih kelola ruang, laporan, atau keluar: ").lower()
        if aksi == "kelola ruang":
            admin.kelola_ruang()
        elif aksi == "laporan":
            dari = baca_waktu("Laporan dari")
            sampai = baca_waktu("Laporan sampai")
            admin.lihat_laporan(dari, sampai)
        elif aksi == "keluar":
            break
