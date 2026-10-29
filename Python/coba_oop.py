from datetime import date


class Buku:
    def __init__(self, judul, stok):
        self.judul = judul
        self.stok = stok

    def pinjam_buku(self):
        if self.stok > 0:
            self.stok -= 1
            print(f"{self.judul} berhasil dipinjam")
            return True
        else:
            print(f"{self.judul} stok habis")
            return False

    def kembalikan_buku(self):
        self.stok += 1
        print(f"{self.judul} telah dikembalikan")


class Peminjam:
    def __init__(self, nama):
        self.nama = nama
        self.daftar_peminjaman = []

    def tambah_peminjaman(self, peminjaman):
        self.daftar_peminjaman.append(peminjaman)


class Peminjaman:
    def __init__(self, buku, peminjam):
        self.buku = buku
        self.peminjam = peminjam
        self.tanggal_pinjam = date.today()
        self.tanggal_kembali = None
        self.denda = 0

    def kembalikan_buku(self):
        self.buku.kembalikan_buku()
        self.tanggal_kembali = date.today()
        print("Buku berhasil dikembalikan")

    def hitung_denda(self, keterlambatan):
        self.denda = keterlambatan * 1000
        return self.denda


# Membuat object Buku
buku1 = Buku("Python Dasar", 3)
buku2 = Buku("Struktur Data", 1)

# Membuat object Peminjam
peminjam1 = Peminjam("Andi")
peminjam2 = Peminjam("Budi")


# Andi meminjam Python Dasar
if buku1.pinjam_buku():
    transaksi1 = Peminjaman(buku1, peminjam1)
    peminjam1.tambah_peminjaman(transaksi1)


# Menampilkan informasi transaksi
print("\n=== DATA PEMINJAMAN ===")
print("Peminjam :", transaksi1.peminjam.nama)
print("Buku     :", transaksi1.buku.judul)
print("Tanggal  :", transaksi1.tanggal_pinjam)
print("Denda    :", transaksi1.denda)


# Menghitung denda karena terlambat 3 hari
denda = transaksi1.hitung_denda(3)

print("\nDenda setelah terlambat 3 hari: Rp", denda)


# Mengembalikan buku
print("\n=== PENGEMBALIAN ===")
transaksi1.kembalikan_buku()

print("Stok sekarang:", buku1.stok)