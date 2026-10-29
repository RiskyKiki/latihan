def uang(kode, pemakaian):
    """Menentukan tarif per MB berdasarkan kode dan pemakaian."""
    if kode == 'R':  # Paket Reguler
        if pemakaian <= 50:
            return 2000
        elif pemakaian <= 80:
            return 4500
        return 6500
    elif kode == 'C':  # Paket Special
        if pemakaian <= 50:
            return 5000
        elif pemakaian <= 80:
            return 7000
        return 10000
    elif kode == 'V':  # Paket VIP
        if pemakaian <= 50:
            return 7500
        elif pemakaian <= 80:
            return 10000
        return 15000
    return None

def hitung(pemakaian, rate_per_mb):
    """Menghitung biaya penggunaan bandwidth."""
    return pemakaian * rate_per_mb

def read_positive_int(prompt):
    """Membaca dan validasi input integer positif."""
    while True:
        s = input(prompt).strip()
        try:
            v = int(s)
            if v > 0:
                return v
            print("Masukkan angka bulat lebih besar dari 0.")
        except ValueError:
            print("Input tidak valid. Masukkan angka bulat.")


def code():
    """Membaca dan validasi kode pelanggan."""
    while True:
        kode = input("Masukkan kode pelanggan (R=Reguler, C=Special, V=VIP): ").strip()
        if uang(kode, 0) is not None:
            return kode.upper()
        print("Kode tidak valid. Masukkan R, C, atau V.")


def read_pemakaian():
    """Membaca dan validasi jumlah pemakaian bandwidth."""
    while True:
        s = input("Masukkan jumlah pemakaian (MB): ").strip()
        try:
            mb = int(s)
            if mb >= 0:
                return mb
            print("Pemakaian harus >= 0.")
        except ValueError:
            print("Input tidak valid. Masukkan angka bulat untuk MB.")


def biaya(kode, usage, rate, total):
    """Menampilkan informasi biaya penggunaan bandwidth."""
    tipe_paket = {'R': 'Paket Reguler', 'C': 'Paket Special', 'V': 'Paket VIP'}
    print("\n" + "="*50)
    print("HASIL PERHITUNGAN BIAYA BANDWIDTH")
    print("="*50)
    print(f"Tipe Paket          : {tipe_paket[kode]}")
    print(f"Kode Paket          : {kode}")
    print(f"Jumlah Pemakaian    : {usage} MB")
    print(f"Tarif per MB        : Rp {rate:,}")
    print(f"Total Biaya         : Rp {total:,}")
    print("="*50)


def main():
    """Fungsi utama program."""
    print("\n" + "="*50)
    print("PROGRAM HITUNG BIAYA BANDWIDTH")
    print("Hotspot Modi")
    print("="*50)
    
    try:
        n = read_positive_int("\nMasukkan jumlah pelanggan (n > 0): ")
        total_biaya_keseluruhan = 0
        
        for i in range(1, n + 1):
            print(f"\n[Pelanggan ke-{i}]")
            kode = code()
            usage = read_pemakaian()
            rate = uang(kode, usage)
            total = hitung(usage, rate)
            total_biaya_keseluruhan += total

        biaya(kode, usage, rate, total)
        
        # Tampilkan ringkasan
        print("\n" + "="*50)
        print("RINGKASAN HASIL PEMROSESAN")
        print("="*50)
        print(f"Total Pelanggan      : {n}")
        print(f"Total Biaya Seluruh  : Rp {total_biaya_keseluruhan:,}")
        print(f"Rata-rata Biaya      : Rp {total_biaya_keseluruhan // n:,}")
        print("="*50)
        print("Terima kasih telah menggunakan layanan kami.")
    
    except KeyboardInterrupt:
        print("\n\nProgram dihentikan pengguna.")


if __name__ == '__main__':
    main()
