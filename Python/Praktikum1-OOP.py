class Barang:
    def __init__(self, kode_barang, nama_barang, harga, stok):
        self.kode_barang = kode_barang
        self.nama_barang = nama_barang
        self.harga = harga
        self.stok = stok

    def hitung_total(self, jumlah):
        if jumlah <= 0:
            print("Jumlah harus lebih dari 0") 
            return 0
        if jumlah > self.stok:
            print(f"Stok barang {self.nama_barang} tidak cukup")
            return 0

        total = self.harga * jumlah
        return total
    
    def kurangi_stok(self, jumlah):
        if jumlah <= 0:
            print("Jumlah harus lebih dari 0")
            return False
        if jumlah > self.stok:
            print(f"Stok barang {self.nama_barang} tidak cukup")
            return False

        self.stok -= jumlah
        print(f"{jumlah} {self.nama_barang} berhasil terjual")
        return True

    def tampilkan_info(self):
        print("\nInformasi Barang")
        print(f"Kode    : {self.kode_barang}")
        print(f"Nama    : {self.nama_barang}")
        print(f"Harga   : {self.harga}")
        print(f"Stok    : {self.stok}")

barang1 = Barang("B001", "Buku", 4000, 5)
barang2 = Barang("B002", "Pensil", 1000, 10)

barang1.tampilkan_info()
barang2.tampilkan_info()


jumlah = int(input(f"\nMasukkan jumlah barang {barang1.nama_barang} yang ingin dibeli:"))

total = barang1.hitung_total(jumlah)

if total > 0:
    print(f"\nTotal harga: {total}")

    if barang1.kurangi_stok(jumlah):
        print("Transaksi berhasil.")

barang1.tampilkan_info()