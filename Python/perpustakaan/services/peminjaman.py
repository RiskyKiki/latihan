class Peminjaman:
    def __init__(self, buku, anggota):
        self.buku = buku
        self.anggota = anggota
        self.status = "menunggu"

    def proses_peminjaman(self):
        # Decision: Stok > 0?
        if self.buku.kurangi_stok():
            self.status = "berhasil"
            return f"Peminjaman {self.buku.judul} berhasil"
        else:
            self.status = "ditolak"
            return f"Stok {self.buku.judul} habis"