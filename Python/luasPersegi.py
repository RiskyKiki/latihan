def luas_persegi_dari_sisi(sisi):
    return sisi * sisi

def luas_persegi_dari_keliling(keliling):
    sisi = keliling / 4
    return sisi * sisi

print("Program Menghitung Luas Persegi")
print("1. Berdasarkan sisi")
print("2. Berdasarkan keliling")
pilihan = input("Pilih metode (1/2): ")

if pilihan == "1":
    sisi = float(input("Masukkan panjang sisi: "))
    luas = luas_persegi_dari_sisi(sisi)
    print(f"Luas persegi adalah {luas}")
elif pilihan == "2":
    keliling = float(input("Masukkan keliling persegi: "))
    luas = luas_persegi_dari_keliling(keliling)
    print(f"Luas persegi adalah {luas}")
else:
    print("Pilihan tidak valid.")
