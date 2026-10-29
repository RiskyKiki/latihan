import math

# ===========================
# FUNGSI
# ===========================

def volume_bola(r):
    return (4/3) * math.pi * r**3

def volume_tabung(r1, t1):
    return math.pi * r1**2 * t1


# ===========================
# PROSEDUR
# ===========================

def hitung_limas(s, t):
    volume = (1/3) * s * s * t
    # tinggi_sisi = math.sqrt((s/2)**2 + t**2)
    # luas_permukaan = (s * s) + 4 * (0.5 * s * tinggi_sisi)
    luas_permukaan = s ** 2 + 2 * s * t

    print("=== HASIL PERHITUNGAN LIMAS ===")
    # print("Volume Limas            :", volume)
    print(f"Volume Limas            :{volume}")
    # print("Luas Permukaan Limas    :", luas_permukaan)
    print(f"Luas Permukaan Limas    :{luas_permukaan}")
    print("\n")


def hitung_balok(p, l, t2):
    volume = p * l * t2
    luas_permukaan = 2 * (p*l + p*t2 + l*t2)
    
    print("=== HASIL PERHITUNGAN BALOK ===")
    # print("Volume Balok            :", volume)
    print(f"Volume Balok            :{volume}")
    # print("Luas Permukaan Balok    :", luas_permukaan)
    print(f"Luas Permukaan Balok    :{luas_permukaan}")
    print("\n")

# ===========================
# CONTOH PEMANGGILAN
# ===========================

def main():
    #Soal A
    #function
    r1 = float(input("Masukkan Jari-jari = "))
    t1 = float(input("Masukkan Tinggi = "))
    print("=== HASIL PERHITUNGAN Tabung ===")
    print(f"Volume Tabung            :{volume_tabung(r1, t1)}")
    print("\n")
    # prosedur
    p = float(input("Masukkan Panjang = "))
    l = float(input("Masukkan Lebar = "))
    t2 = float(input("Masukkan Tinggi = "))
    hitung_balok(p, l, t2)

    #soal B
    #function
    r = float(input("Masukkan Jari-jari = "))
    print("=== HASIL PERHITUNGAN Bola ===")
    print(f"Volume Bola            :{volume_bola(r)}")
    print("\n")
    #prosedur
    s = float(input("Masukkan Sisi = "))
    t = float(input("Masukkan Tinggi = "))
    hitung_limas(s, t)
    
main()