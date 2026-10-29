class Buku:
    def __init__(self, kode_buku, judul, stok):
        self.kode_buku = kode_buku
        self.judul = judul
        self.stok = stok

    # @property
    # def stok(self):
    #     return self.__stok

    # @stok.setter
    # def stok(self, value):
    #     raise ValueError("Stok tidak boleh dirubah") 

    def kurangi_stok(self):
        if self.stok > 0:
            self.stok -= 1
            return True
        return False
    
    def tambah_stok(self, jumlah=1):
        self.stok += jumlah