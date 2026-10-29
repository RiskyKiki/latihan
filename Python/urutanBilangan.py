# Program untuk mengurutkan 3 bilangan yang diinput pengguna
# Output akan menampilkan susunan bilangan secara ascending (menaik)
# dan descending (menurun).
# Komentar di dalam kode menjelaskan tiap langkah.


def read_number(prompt):
    """Baca input dari pengguna dan validasi sebagai bilangan (float).
    Jika input kosong atau tidak bisa dikonversi, minta ulang.
    Mengembalikan nilai float.
    """
    while True:
        s = input(prompt).strip()
        if s == "":
            print("Input tidak boleh kosong. Coba lagi.")
            continue
        try:
            # Gunakan float agar program menerima bilangan desimal juga
            return float(s)
        except ValueError:
            print("Input tidak valid. Masukkan bilangan (contoh: 3, 4.5, -2).")


if __name__ == '__main__':
    print("Program Mengurutkan 3 Bilangan")
    print("------------------------------")

    # Baca tiga bilangan dari pengguna
    a = read_number("Masukkan bilangan pertama: ")
    b = read_number("Masukkan bilangan kedua  : ")
    c = read_number("Masukkan bilangan ketiga : ")

    # Simpan dalam list untuk kemudahan pengurutan
    nums = [a, b, c]

    # Urutkan ascending (menaik)
    ascending = sorted(nums)  # built-in sorted mengembalikan list baru yang terurut

    # Urutkan descending (menurun)
    descending = sorted(nums, reverse=True)

    # Tampilkan hasil dengan format yang rapi
    print("\nHasil pengurutan:")
    print("Ascending  : ", ", ".join(map(lambda x: str(x).rstrip('0').rstrip('.') if isinstance(x, float) else str(x), ascending)))
    print("Descending : ", ", ".join(map(lambda x: str(x).rstrip('0').rstrip('.') if isinstance(x, float) else str(x), descending)))

    # Penjelasan singkat (komentar pengguna)
    print("\nPenjelasan singkat:")
    print("- Program membaca tiga bilangan dari input pengguna.")
    print("- Kemudian menggunakan fungsi sorted() untuk membuat versi terurut dari list.")
    print("- 'ascending' berisi list terurut menaik, 'descending' berisi versi menurun.")
    print("- Hasil dicetak dalam format yang mudah dibaca.")
