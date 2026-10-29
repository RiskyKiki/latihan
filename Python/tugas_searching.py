# SOAL 1 - Linear Search data mahasiswa berdasarkan NPM
DAFTAR_MAHASISWA = [
    ("1234", "Vara", "2A"),
    ("1235", "Amel", "2B"),
    ("1236", "Aurel", "2C"),
    ("1237", "Raya", "2D"),
    ("1238", "Azzam", "2A"),
    ("1239", "Zahra", "2B"),
    ("1240", "Najwa", "2C"),
]


def cari_mahasiswa(npm_dicari):
    """Mencari mahasiswa berdasarkan NPM dengan Linear Search."""
    for mahasiswa in DAFTAR_MAHASISWA:
        if mahasiswa[0] == npm_dicari:
            return mahasiswa
    return None


def jalankan_pencarian_mahasiswa():
    npm = input("Masukkan NPM yang dicari (4 digit): ").strip()
    if len(npm) != 4 or not npm.isdigit():
        print("NPM harus terdiri dari 4 digit.")
        return

    mahasiswa = cari_mahasiswa(npm)
    if mahasiswa is None:
        print("Mahasiswa dengan NPM tersebut tidak ditemukan.")
    else:
        print(f"NPM: {mahasiswa[0]}")
        print(f"Nama: {mahasiswa[1]}")
        print(f"Kelas: {mahasiswa[2]}")


# SOAL 2 - Binary Search data buku berdasarkan kode
DAFTAR_BUKU = [
    ("063", "The C++ Programming", "James Wood"),
    ("025", "Mastering Delphi 6", "Marcopolo"),
    ("096", "Professional C#", "Simon Webe"),
    ("056", "Pure JavaScript v2", "Michael Bolton"),
    ("041", "Advanced JSP & Servlet", "David Dunn"),
    ("034", "Calculus Make it Easy", "Gunner Christian"),
    ("088", "Visual Basic 2005 Express", "Antonie"),
    ("072", "Artificial Life : Volume 1", "Gloria Virginia"),
]


def cari_buku(kode_dicari):
    """Mencari buku berdasarkan kode dengan Binary Search."""
    buku_urut = sorted(DAFTAR_BUKU, key=lambda buku: buku[0])

    def cari_rekursif(kiri, kanan):
        if kiri > kanan:
            return None

        tengah = (kiri + kanan) // 2
        kode_tengah = buku_urut[tengah][0]

        if kode_tengah == kode_dicari:
            return buku_urut[tengah]
        if kode_dicari < kode_tengah:
            return cari_rekursif(kiri, tengah - 1)
        return cari_rekursif(tengah + 1, kanan)

    return cari_rekursif(0, len(buku_urut) - 1)


def jalankan_pencarian_buku():
    kode = input("Masukkan kode buku yang dicari (3 digit): ").strip()
    if len(kode) != 3 or not kode.isdigit():
        print("Kode buku harus terdiri dari 3 digit.")
        return

    buku = cari_buku(kode)
    if buku is None:
        print("Buku dengan kode tersebut tidak ditemukan.")
    else:
        print(f"Kode: {buku[0]}")
        print(f"Judul buku: {buku[1]}")
        print(f"Pengarang: {buku[2]}")


if __name__ == "__main__":
    jalankan_pencarian_mahasiswa()
    print("\n--- Soal 1 selesai. Sekarang lanjut ke Soal 2 ---\n")
    jalankan_pencarian_buku()
