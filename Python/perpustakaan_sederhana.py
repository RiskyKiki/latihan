# Program perpustakaan sederhana menggunakan list of tuples.
# Setiap buku disimpan sebagai tuple (judul, penulis, tahun).
buku = [
    ("Belajar Python", "Andi", 2021),
    ("Algoritma Dasar", "Budi", 2019),
    ("Pemrograman Terapan", "Citra", 2023),
    ("Data Science untuk Pemula", "Dewi", 2022),
    ("Machine Learning Lanjutan", "Eka", 2024),
    ("Web Development dengan Python", "Fajar", 2020)
]

# Jika ingin memulai dengan daftar buku kosong, uncomment baris dibawah dan comment baris diatas
# buku = [
#
# ]

def tampilkan_daftar():
    if not buku:
        print("Daftar buku kosong.")
        return

    print("\n=== DAFTAR BUKU ===")
    for index, (judul, penulis, tahun) in enumerate(buku, start=1):
        print(f"{index}. {judul} | {penulis} | {tahun}")


def tambah_buku():
    # Minta input pengguna dan tambahkan tuple buku ke dalam list.
    judul = input("Judul buku: ").strip()
    penulis = input("Penulis: ").strip()
    try:
        tahun = int(input("Tahun terbit: "))
    except ValueError:
        print("Tahun tidak valid. Gunakan angka.")
        return

    buku.append((judul, penulis, tahun))
    print(f"Buku '{judul}' berhasil ditambahkan.")


def hapus_buku():
    # Cari buku berdasarkan judul dan hapus tuple yang cocok.
    judul = input("Masukkan judul buku yang akan dihapus: ").strip().lower()
    for item in buku:
        if item[0].lower() == judul:
            buku.remove(item)
            print(f"Buku '{item[0]}' berhasil dihapus.")
            return
    print("Buku tidak ditemukan.")


def cari_buku():
    judul = input("Masukkan judul buku yang dicari: ").strip().lower()
    hasil = [item for item in buku if judul in item[0].lower()]

    if not hasil:
        print("Buku tidak ditemukan.")
        return

    print("\nHasil pencarian:")
    for judul, penulis, tahun in hasil:
        print(f"- {judul} | {penulis} | {tahun}")


def tampilkan_setelah_2020():
    hasil = [(judul, penulis, tahun) for judul, penulis, tahun in buku if tahun > 2020]

    if not hasil:
        print("Tidak ada buku terbit setelah 2020.")
        return

    print("\nBuku terbit setelah 2020:")
    for judul, penulis, tahun in hasil:
        print(f"- {judul} | {penulis} | {tahun}")


def main():
    while True:
        print("\n=== PERPUSTAKAAN SEDERHANA ===")
        print("1. Tampilkan semua buku")
        print("2. Tambah buku")
        print("3. Hapus buku")
        print("4. Cari buku berdasarkan judul")
        print("5. Tampilkan buku terbitan > 2020")
        print("6. Keluar")

        pilihan = input("Pilih menu (1-6): ")

        match pilihan:
            case '1':
                tampilkan_daftar()
            case '2':
                tambah_buku()
            case '3':
                hapus_buku()
            case '4':
                cari_buku()
            case '5':
                tampilkan_setelah_2020()
            case '6':
                print("Terima kasih. Keluar dari program.")
                break
            case _:
                print("Pilihan tidak valid. Coba lagi.")

main()