# daftar berupa list untuk menyimpan item belanja
daftar = []

# fungsi untuk menambahkan item ke daftar belanja
def tambah_item(nama, harga, jumlah):
    # Membuat dictionary untuk menyimpan 1 item
    item = {
        'nama': nama,
        'harga': harga,
        'jumlah': jumlah
    }
    # append() menambah item ke akhir list
    daftar.append(item)
    print(f"'{nama}' ditambahkan ke daftar")

# procedure untuk menampilkan semua item dalam daftar belanja
def lihat_daftar():
    print("\n--- DAFTAR BELANJA ---")
    
    # jika daftar kosong
    # len(daftar) == 0 artinya: daftar tidak memiliki elemen (panjang = 0)
    if len(daftar) == 0:
        print("Daftar belanja kosong")
        return
    
    # menampilkan setiap item dengan nomor urut
    for i, item in enumerate(daftar, 1):
        total_item = item['harga'] * item['jumlah']
        print(f"{i}. {item['nama']}")
        print(f"   Harga: Rp{item['harga']} x {item['jumlah']} = Rp{total_item}")

# fungsi untuk menghitung total harga seluruh belanja (return value)
def hitung_total():
    # jika daftar kosong, return 0
    # len(daftar) == 0 digunakan untuk cek apakah list kosong
    if len(daftar) == 0:
        return 0
    
    # menghitung total dengan loop
    total = 0
    for item in daftar:
        total += item['harga'] * item['jumlah']
    
    return total


# main program 
while True:
    print("\n===== MENU DAFTAR BELANJA =====")
    print("1. Tambah Item")
    print("2. Lihat Daftar")
    print("3. Hitung Total")
    print("4. Keluar")
    
    pilihan = input("\nPilih menu (1-4): ")
    
    if pilihan == '1':
        nama = input("Nama barang: ")
        harga = float(input("Harga barang: "))
        jumlah = int(input("Jumlah: "))
        tambah_item(nama, harga, jumlah)
    
    elif pilihan == '2':
        lihat_daftar()
    
    elif pilihan == '3':
        total_belanja = hitung_total()
        print(f"\n--- TOTAL BELANJA ---")
        print(f"Total: Rp{total_belanja}")
    
    elif pilihan == '4':
        print("Terima kasih! Sampai jumpa.")
        break
    
    else:
        print("Pilihan tidak valid!")
