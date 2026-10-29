from models.buku import Buku
from models.anggota import Anggota
from services.peminjaman import Peminjaman

buku1 = Buku("B01", "Pemrograman Python", 1)

anggota1 = Anggota("A01", "Sari")
peminjaman1 = Peminjaman(buku1, anggota1)

print(f"Status: {peminjaman1.status}")
print(peminjaman1.proses_peminjaman())
print(f"Status: {peminjaman1.status}")
print()
print(peminjaman1.proses_peminjaman())
print(f"Status: {peminjaman1.status}")
