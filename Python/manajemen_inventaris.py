# ==============================================================================
# PROGRAM: SISTEM MANAJEMEN INVENTARIS GUDANG & KASIR TOKO (INTERAKTIF)
# Bahasa Pemrograman: Python 3
# File: manajemen_inventaris.py
#
# Program ini dibuat untuk mendemonstrasikan berbagai logika dasar pemrograman Python,
# struktur data List dan Tuple, fungsi, prosedur, rekursi, serta penekanan khusus
# pada seluruh Built-in Method (fungsi bawaan) dari tipe data List.
# ==============================================================================

# ------------------------------------------------------------------------------
# 1. STRUKTUR DATA UTAMA
# ------------------------------------------------------------------------------

# TUPLE: Bersifat Immutable (tidak bisa diubah), cocok untuk kategori produk yang tetap
KATEGORI_PRODUK = ("Elektronik", "Makanan", "Pakaian", "Alat Tulis")

# LIST: Bersifat Mutable (bisa diubah), menyimpan daftar barang inventaris saat ini
# Format barang: [Nama Barang, Kategori, Harga (Rp), Stok]
inventaris = [
    ["Laptop Asus", "Elektronik", 12000000, 10],
    ["Roti Tawar", "Makanan", 15000, 50],
    ["Kemeja Flanel", "Pakaian", 150000, 30],
    ["Buku Tulis", "Alat Tulis", 8000, 100],
    ["Mouse Wireless", "Elektronik", 250000, 20]
]

# LIST: Keranjang belanja kasir
keranjang_belanja = []

# LIST: Log catatan riwayat aktivitas program
log_aktivitas = ["Sistem diaktifkan", "Database inventaris awal dimuat"]

# ------------------------------------------------------------------------------
# 2. FUNGSI DAN PROSEDUR (FUNCTION & PROCEDURE)
# ------------------------------------------------------------------------------

def tambah_log(pesan):
    """
    [Prosedur] Menambahkan catatan aktivitas ke dalam list log_aktivitas.
    Prosedur tidak mengembalikan nilai (None), melainkan memodifikasi log global.
    """
    log_aktivitas.append(pesan)


def tampilkan_header():
    """
    [Prosedur] Menampilkan header aplikasi.
    """
    print("\n" + "=" * 65)
    print("        SISTEM MANAJEMEN INVENTARIS & KASIR GUDANG MANDIRI       ")
    print("=" * 65)


def tampilkan_menu_utama():
    """
    [Prosedur] Menampilkan daftar menu utama.
    """
    print("\n--- MENU UTAMA ---")
    print("1. Lihat Semua Inventaris Gudang & Pengelompokan Kategori")
    print("2. Demo Operasi List (Built-in Method)")
    print("3. Kasir (Simulasi Keranjang Belanja)")
    print("4. Hitung Total Nilai Aset Gudang (Rekursi)")
    print("5. Lihat Log Aktivitas Toko")
    print("6. Keluar dari Program")
    print("-" * 30)


def input_angka_valid(prompt):
    """
    [Fungsi] Meminta input angka integer dari user dengan validasi agar tidak error.
    Mengembalikan nilai integer.
    """
    while True:
        input_user = input(prompt)
        if input_user.isdigit():
            return int(input_user)
        else:
            print("[ERROR] Input harus berupa angka positif! Silakan coba lagi.")


def tampilkan_inventaris():
    """
    [Prosedur] Menampilkan seluruh daftar barang yang ada di gudang.
    Mendemonstrasikan LOOPING (for) dan BRANCHING (if-else).
    """
    print("\n--- DAFTAR INVENTARIS GUDANG SAAT INI ---")
    if len(inventaris) == 0:
        print("(Gudang kosong, tidak ada barang)")
        return
    
    print(f"{'No':<4} | {'Nama Barang':<20} | {'Kategori':<15} | {'Harga':<15} | {'Stok':<6}")
    print("-" * 65)
    
    # Looping 'for' untuk membaca list inventaris
    for indeks, barang in enumerate(inventaris):
        # barang[0] = Nama, barang[1] = Kategori, barang[2] = Harga, barang[3] = Stok
        # Branching if-else untuk memberi tanda jika stok menipis
        status_stok = ""
        if barang[3] <= 5:
            status_stok = " (HAMPIR HABIS!)"
            
        print(f"{indeks:<4} | {barang[0]:<20} | {barang[1]:<15} | Rp{barang[2]:<12,} | {barang[3]}{status_stok}")
    print("-" * 65)


def tampilkan_barang_per_kategori():
    """
    [Prosedur] Menampilkan barang yang dikelompokkan berdasarkan kategorinya.
    Mendemonstrasikan NESTED LOOP (For di dalam For) dan pengaksesan data Tuple.
    """
    print("\n--- PENGELOMPOKAN BARANG BERDASARKAN KATEGORI ---")
    
    # Outer Loop: Iterasi melewati Tuple Kategori (Immutable)
    for kat in KATEGORI_PRODUK:
        print(f"\n>> Kategori: {kat}")
        ada_barang = False
        
        # Inner Loop: Iterasi mencari barang di List Inventaris yang sesuai kategori
        for barang in inventaris:
            if barang[1] == kat:
                print(f"   * {barang[0]} - Harga: Rp{barang[2]:,} - Stok: {barang[3]}")
                ada_barang = True
                
        # Branching if untuk menampilkan pesan jika kategori kosong
        if not ada_barang:
            print("     (Tidak ada barang di kategori ini)")


# ------------------------------------------------------------------------------
# 3. REKURSI (RECURSION)
# ------------------------------------------------------------------------------

def hitung_total_aset_rekursif(daftar_barang, indeks=0):
    """
    [Fungsi Rekursif] Menghitung total nilai aset seluruh barang di gudang.
    Rumus total aset = Jumlah dari semua (Harga * Stok) barang.
    """
    # Basis Kasus (Base Case): Jika indeks melampaui jumlah barang
    if indeks == len(daftar_barang):
        return 0
    
    # Langkah Rekursif (Recursion Step):
    # Dapatkan nilai aset barang saat ini (Harga * Stok)
    nilai_barang_sekarang = daftar_barang[indeks][2] * daftar_barang[indeks][3]
    
    # Panggil fungsi dirinya sendiri dengan menaikkan indeks
    return nilai_barang_sekarang + hitung_total_aset_rekursif(daftar_barang, indeks + 1)


# ------------------------------------------------------------------------------
# 4. KASIR & KERANJANG BELANJA
# ------------------------------------------------------------------------------

def menu_kasir():
    """
    [Prosedur] Mengelola proses simulasi pembelian kasir.
    Menggunakan WHILE loop, NESTED IF, BREAK, CONTINUE, dan list.
    """
    tambah_log("Membuka menu Kasir")
    # Emulasi Do-While menggunakan while True dan break di akhir iterasi
    while True:
        print("\n=== MENU SIMULASI KASIR ===")
        print("1. Tambah Barang ke Keranjang")
        print("2. Lihat Keranjang Belanja")
        print("3. Kosongkan Keranjang (.clear)")
        print("4. Checkout & Bayar")
        print("5. Kembali ke Menu Utama")
        pilihan = input("Pilih Menu Kasir (1-5): ")
        
        if pilihan == "1":
            tampilkan_inventaris()
            no_barang = input_angka_valid("Masukkan Nomor Urut Barang (indeks): ")
            
            # Nested If untuk validasi range indeks list
            if 0 <= no_barang < len(inventaris):
                barang_terpilih = inventaris[no_barang]
                jumlah = input_angka_valid(f"Masukkan jumlah '{barang_terpilih[0]}' yang ingin dibeli: ")
                
                # Nested If untuk cek stok
                if jumlah <= barang_terpilih[3]:
                    # Kurangi stok gudang
                    inventaris[no_barang][3] -= jumlah
                    
                    # Tambah ke keranjang belanja [Nama, Harga, Jumlah, Total]
                    total_harga = barang_terpilih[2] * jumlah
                    keranjang_belanja.append([barang_terpilih[0], barang_terpilih[2], jumlah, total_harga])
                    print(f"\n[SUKSES] {jumlah} {barang_terpilih[0]} dimasukkan ke keranjang belanja!")
                    tambah_log(f"Menambah {jumlah} {barang_terpilih[0]} ke keranjang")
                else:
                    print(f"\n[GAGAL] Stok tidak mencukupi! Stok saat ini: {barang_terpilih[3]}")
            else:
                print("\n[ERROR] Nomor indeks barang tidak ditemukan!")
                
        elif pilihan == "2":
            print("\n--- ISI KERANJANG BELANJA ---")
            if len(keranjang_belanja) == 0:
                print("(Keranjang masih kosong)")
                continue # Langsung lanjut ke iterasi loop berikutnya
                
            print(f"{'Nama':<20} | {'Harga Satuan':<15} | {'Jumlah':<8} | {'Subtotal':<15}")
            print("-" * 65)
            total_bayar = 0
            for item in keranjang_belanja:
                print(f"{item[0]:<20} | Rp{item[1]:<12,} | {item[2]:<8} | Rp{item[3]:<12,}")
                total_bayar += item[3]
            print("-" * 65)
            print(f"Total Sementara: Rp{total_bayar:,}")
            
        elif pilihan == "3":
            # Mendemonstrasikan method bawaan list .clear()
            if len(keranjang_belanja) > 0:
                # Mengembalikan stok terlebih dahulu sebelum dihapus
                for item in keranjang_belanja:
                    for barang in inventaris:
                        if barang[0] == item[0]:
                            barang[3] += item[2] # Kembalikan stok
                
                print(f"Keranjang belanja berisi {len(keranjang_belanja)} item akan dikosongkan.")
                keranjang_belanja.clear() # MENGOSONGKAN LIST
                print("[SUKSES] Keranjang belanja telah dikosongkan (.clear() berhasil dijalankan)!")
                tambah_log("Mengosongkan keranjang belanja")
            else:
                print("[INFO] Keranjang belanja memang sudah kosong.")
                
        elif pilihan == "4":
            if len(keranjang_belanja) == 0:
                print("[INFO] Keranjang kosong, tidak ada transaksi untuk dicheckout.")
                continue
            
            total_bayar = sum([item[3] for item in keranjang_belanja])
            print(f"\nTotal Tagihan: Rp{total_bayar:,}")
            uang = input_angka_valid("Masukkan Uang Pembayaran: Rp")
            
            if uang >= total_bayar:
                kembalian = uang - total_bayar
                print(f"Pembayaran Sukses! Kembalian Anda: Rp{kembalian:,}")
                keranjang_belanja.clear()
                print("Terima kasih telah berbelanja!")
                tambah_log(f"Transaksi kasir selesai. Total bayar: Rp{total_bayar:,}")
                break # Keluar dari menu kasir kembali ke menu utama
            else:
                print("[GAGAL] Uang pembayaran tidak cukup!")
                
        elif pilihan == "5":
            break # Keluar dari loop kasir
        else:
            print("[ERROR] Pilihan tidak valid! Silakan masukkan angka 1-5.")


# ------------------------------------------------------------------------------
# 5. DEMONSTRASI BULK & BUILT-IN METHOD LIST PYTHON
# ------------------------------------------------------------------------------

def menu_demonstrasi_list():
    """
    [Prosedur] Menyediakan interaksi langsung untuk mendemonstrasikan secara detail
    berbagai Built-in Method bawaan dari struktur data LIST di Python.
    """
    while True:
        print("\n========================================================")
        print("          DEMONSTRASI BUILT-IN METHOD LIST PYTHON       ")
        print("========================================================")
        print("1.  .append()  -> Tambah barang baru di akhir list")
        print("2.  .insert()  -> Sisipkan barang prioritas pada indeks tertentu")
        print("3.  .remove()  -> Hapus barang tertentu berdasarkan nama")
        print("4.  .pop()     -> Hapus & ambil barang berdasarkan indeks")
        print("5.  .index()   -> Cari indeks (posisi) dari suatu barang")
        print("6.  .count()   -> Hitung jumlah barang dalam kategori tertentu")
        print("7.  .sort()    -> Urutkan barang berdasarkan HARGA secara permanen")
        print("8.  .reverse() -> Balikkan urutan list barang saat ini")
        print("9.  .extend()  -> Tambahkan daftar barang baru secara massal (bulk)")
        print("10. .copy()    -> Buat backup database inventaris (Shallow Copy)")
        print("11. Kembali ke Menu Utama")
        print("========================================================")
        
        pilihan = input("Pilih Operasi List (1-11): ")
        
        # Penggunaan MATCH-CASE (Python Switch-Case)
        match pilihan:
            case "1":
                print("\n--- DEMO: .append(elemen) ---")
                nama = input("Masukkan Nama Barang Baru: ")
                
                # Menampilkan opsi Kategori menggunakan loop tuple KATEGORI_PRODUK
                print("Pilihan Kategori:")
                for k in KATEGORI_PRODUK:
                    print(f"- {k}")
                kategori = input("Masukkan Kategori: ")
                
                # Validasi kategori menggunakan operator keanggotaan 'in'
                if kategori not in KATEGORI_PRODUK:
                    print("[GAGAL] Kategori tidak valid!")
                    continue
                
                harga = input_angka_valid("Masukkan Harga (Rp): ")
                stok = input_angka_valid("Masukkan Stok Awal: ")
                
                barang_baru = [nama, kategori, harga, stok]
                print(f"Sebelum .append(): Total barang = {len(inventaris)}")
                
                # Eksekusi built-in method .append()
                inventaris.append(barang_baru)
                
                print(f"Setelah .append(): Total barang = {len(inventaris)}")
                print(f"[INFO] Barang '{nama}' sukses ditambahkan ke akhir list!")
                tambah_log(f"Menambahkan '{nama}' via .append()")
                
            case "2":
                print("\n--- DEMO: .insert(indeks, elemen) ---")
                tampilkan_inventaris()
                indeks = input_angka_valid(f"Masukkan indeks penempatan (0 - {len(inventaris)}): ")
                
                if 0 <= indeks <= len(inventaris):
                    nama = input("Masukkan Nama Barang Prioritas: ")
                    print("Pilihan Kategori:")
                    for k in KATEGORI_PRODUK:
                        print(f"- {k}")
                    kategori = input("Masukkan Kategori: ")
                    
                    if kategori not in KATEGORI_PRODUK:
                        print("[GAGAL] Kategori tidak valid!")
                        continue
                        
                    harga = input_angka_valid("Masukkan Harga (Rp): ")
                    stok = input_angka_valid("Masukkan Stok Awal: ")
                    
                    barang_baru = [nama, kategori, harga, stok]
                    
                    # Eksekusi built-in method .insert()
                    inventaris.insert(indeks, barang_baru)
                    
                    print(f"[INFO] Barang '{nama}' sukses disisipkan pada indeks ke-{indeks}!")
                    tambah_log(f"Menyisipkan '{nama}' pada indeks {indeks} via .insert()")
                else:
                    print("[GAGAL] Indeks di luar jangkauan!")
                    
            case "3":
                print("\n--- DEMO: .remove(elemen) ---")
                tampilkan_inventaris()
                nama_hapus = input("Masukkan NAMA BARANG yang ingin dihapus tepat: ")
                
                # Mencari objek barang dalam list terlebih dahulu karena remove memerlukan objek asli
                barang_ketemu = None
                for barang in inventaris:
                    if barang[0].lower() == nama_hapus.lower():
                        barang_ketemu = barang
                        break
                
                if barang_ketemu is not None:
                    print(f"Mencoba menghapus: {barang_ketemu}")
                    
                    # Eksekusi built-in method .remove()
                    inventaris.remove(barang_ketemu)
                    
                    print("[SUKSES] Barang berhasil dihapus dari list menggunakan .remove()!")
                    tambah_log(f"Menghapus '{barang_ketemu[0]}' via .remove()")
                else:
                    print("[GAGAL] Nama barang tidak ditemukan! Perhatikan huruf besar/kecil.")
                    
            case "4":
                print("\n--- DEMO: .pop(indeks) ---")
                tampilkan_inventaris()
                print("Catatan: Jika indeks dikosongkan, pop() otomatis menghapus elemen TERAKHIR.")
                pilihan_indeks = input(f"Masukkan indeks yang ingin dihapus (0 - {len(inventaris)-1}) [Kosongkan jika ingin elemen terakhir]: ")
                
                try:
                    if pilihan_indeks == "":
                        # Eksekusi .pop() tanpa parameter (menghapus item terakhir)
                        barang_dihapus = inventaris.pop()
                        print(f"[SUKSES] Menghapus elemen terakhir: {barang_dihapus[0]} menggunakan .pop()")
                        tambah_log(f"Menghapus barang terakhir via .pop()")
                    else:
                        idx = int(pilihan_indeks)
                        if 0 <= idx < len(inventaris):
                            # Eksekusi .pop(indeks) dengan spesifikasi indeks
                            barang_dihapus = inventaris.pop(idx)
                            print(f"[SUKSES] Menghapus elemen indeks ke-{idx}: {barang_dihapus[0]} menggunakan .pop({idx})")
                            tambah_log(f"Menghapus barang di indeks {idx} via .pop()")
                        else:
                            print("[GAGAL] Indeks tidak valid!")
                except ValueError:
                    print("[ERROR] Input indeks tidak valid!")
                    
            case "5":
                print("\n--- DEMO: .index(elemen) ---")
                # Kita akan mendemonstrasikan pencarian indeks pada list nama barang
                daftar_nama = [barang[0] for barang in inventaris]
                print(f"List Nama Barang saat ini: {daftar_nama}")
                nama_cari = input("Ketik nama barang persis untuk mencari posisi indeksnya: ")
                
                try:
                    # Eksekusi built-in method .index()
                    posisi = daftar_nama.index(nama_cari)
                    print(f"[SUKSES] Nama '{nama_cari}' ditemukan pada indeks ke-{posisi}!")
                    print(f"Data lengkap barang: {inventaris[posisi]}")
                except ValueError:
                    print(f"[GAGAL] '{nama_cari}' tidak ditemukan dalam list nama. Pastikan nama sama persis.")
                    
            case "6":
                print("\n--- DEMO: .count(elemen) ---")
                # Kita akan mendemonstrasikan .count() pada daftar kategori barang
                daftar_kategori = [barang[1] for barang in inventaris]
                print("Daftar kategori pada semua barang:")
                print(daftar_kategori)
                
                print("\nPilih kategori yang ingin dihitung:")
                for k in KATEGORI_PRODUK:
                    print(f"- {k}")
                kat_hitung = input("Kategori yang ingin dihitung: ")
                
                # Eksekusi built-in method .count()
                jumlah = daftar_kategori.count(kat_hitung)
                print(f"[HASIL] Kategori '{kat_hitung}' muncul sebanyak {jumlah} kali dalam list inventaris.")
                
            case "7":
                print("\n--- DEMO: .sort(key) ---")
                print("Mengurutkan barang berdasarkan HARGA secara MENINGKAT (Ascending).")
                print("Sebelum di-sort:")
                tampilkan_inventaris()
                
                # Eksekusi built-in method .sort() menggunakan argumen lambda untuk mengurutkan sub-list
                # x[2] merujuk pada Harga barang
                inventaris.sort(key=lambda x: x[2])
                
                print("\nSetelah di-sort (.sort(key=lambda x: x[2])):")
                tampilkan_inventaris()
                tambah_log("Mengurutkan database inventaris via .sort()")
                
            case "8":
                print("\n--- DEMO: .reverse() ---")
                print("Membalikkan urutan list barang secara permanen.")
                print("Sebelum di-reverse:")
                tampilkan_inventaris()
                
                # Eksekusi built-in method .reverse()
                inventaris.reverse()
                
                print("\nSetelah di-reverse (.reverse()):")
                tampilkan_inventaris()
                tambah_log("Membalikkan urutan inventaris via .reverse()")
                
            case "9":
                print("\n--- DEMO: .extend(iterable) ---")
                # Mendefinisikan list baru yang berisi barang massal untuk dimasukkan ke inventaris
                barang_baru_bulk = [
                    ["Buku Gambar", "Alat Tulis", 12000, 45],
                    ["Celana Jeans", "Pakaian", 220000, 15]
                ]
                print("Daftar barang baru yang akan dimasukkan massal:")
                for b in barang_baru_bulk:
                    print(f"- {b[0]} (Kategori: {b[1]}, Harga: Rp{b[2]:,}, Stok: {b[3]})")
                
                input("\nTekan ENTER untuk menggabungkan barang massal menggunakan .extend()...")
                
                # Eksekusi built-in method .extend()
                inventaris.extend(barang_baru_bulk)
                
                print("[SUKSES] Barang baru berhasil di-extend ke database inventaris!")
                tampilkan_inventaris()
                tambah_log("Melakukan bulk import barang via .extend()")
                
            case "10":
                print("\n--- DEMO: .copy() ---")
                print("Membuat cadangan (backup) list inventaris saat ini.")
                
                # Eksekusi built-in method .copy()
                cadangan_inventaris = inventaris.copy()
                
                # Memverifikasi bahwa kedua list memiliki referensi memori yang berbeda
                print(f"ID List Utama: {id(inventaris)}")
                print(f"ID List Cadangan: {id(cadangan_inventaris)}")
                
                if id(inventaris) != id(cadangan_inventaris):
                    print("[SUKSES] Salinan berhasil dibuat!")
                    print("List utama dan list cadangan tersimpan di alamat memori yang BERBEDA (Shallow Copy berhasil).")
                    print(f"Jumlah barang di list cadangan: {len(cadangan_inventaris)}")
                    tambah_log("Membuat backup inventaris via .copy()")
                else:
                    print("[GAGAL] Salinan gagal dibuat.")
                    
            case "11":
                break # Keluar dari menu demonstrasi list kembali ke menu utama
            case _:
                print("[ERROR] Pilihan menu tidak valid! Masukkan angka 1-11.")


# ------------------------------------------------------------------------------
# 6. LOG ALUR UTAMA (MAIN LOOP PROGRAM)
# ------------------------------------------------------------------------------

def main():
    running = True
    tambah_log("Sesi menu utama dimulai")
    
    while running:
        tampilkan_header()
        tampilkan_menu_utama()
        pilihan = input("Pilih Menu Utama (1-6): ")
        
        # Penggunaan BRANCHING (if-elif-else) untuk navigasi utama
        if pilihan == "1":
            tampilkan_inventaris()
            tampilkan_barang_per_kategori()
            
        elif pilihan == "2":
            menu_demonstrasi_list()
            
        elif pilihan == "3":
            menu_kasir()
            
        elif pilihan == "4":
            print("\n--- PERHITUNGAN TOTAL NILAI ASET GUDANG (REKURSI) ---")
            # Memanggil fungsi rekursif hitung_total_aset_rekursif
            total_aset = hitung_total_aset_rekursif(inventaris)
            print(f"Perhitungan selesai dilakukan.")
            print(f"-> Total nilai seluruh aset barang di gudang saat ini: Rp{total_aset:,}")
            tambah_log(f"Menghitung total aset rekursif: Rp{total_aset:,}")
            
        elif pilihan == "5":
            print("\n--- LOG AKTIVITAS TOKO ---")
            # Looping untuk melihat log
            for i, log in enumerate(log_aktivitas, start=1):
                print(f"[{i:02d}] {log}")
            print("-" * 30)
            
        elif pilihan == "6":
            print("\nTerima kasih telah menggunakan Sistem Manajemen Inventaris Gudang!")
            print("Keluar dari program...")
            running = False # Menghentikan loop utama
            
        else:
            print("[ERROR] Pilihan menu tidak valid! Silakan masukkan angka 1-6.")

# Memulai eksekusi program jika dijalankan sebagai script utama
if __name__ == "__main__":
    main()
