def uang(kode, pemakaian):
    """Menentukan tarif per m3 berdasarkan kode dan pemakaian."""
    if kode == 'F':  # Fasilitas Umum
        if pemakaian <= 50:
            return 3000
        elif pemakaian <= 100:
            return 5000
        return 8000
    elif kode == 'R':  # Rumahan
        if pemakaian <= 50:
            return 4000
        elif pemakaian <= 100:
            return 7000
        return 10000
    elif kode == 'N':  # Niaga
        if pemakaian <= 50:
            return 7500
        elif pemakaian <= 100:
            return 10000
        return 12500
    return None
    
def hitung(pemakaian, tarif):
    """Menghitung biaya retribusi air."""
    return pemakaian * tarif

def total(kode, pemakaian, tarif, biaya):
    """Menampilkan informasi biaya retribusi."""
    tipe_pelanggan = {'F': 'Fasilitas Umum', 'R': 'Rumahan', 'N': 'Niaga'}
    print("\n" + "="*50)
    print("HASIL PERHITUNGAN BIAYA RETRIBUSI AIR")
    print("="*50)
    print(f"Tipe Pelanggan       : {tipe_pelanggan[kode]}")
    print(f"Kode Pelanggan       : {kode}")
    print(f"Jumlah Pemakaian     : {pemakaian} m³")
    print(f"Tarif per m³         : Rp {tarif:,}")
    print(f"Total Biaya          : Rp {biaya:,}")
    print("="*50)

def code():
    """Membaca dan validasi kode pelanggan."""
    while True:
        kode = input("Masukkan kode pelanggan (F/R/N): ").strip().upper()
        if kode in ['F', 'R', 'N']:
            return kode
        print("Kode pelanggan tidak valid. Masukkan F, R, atau N.")

def jumlah():
    """Membaca dan validasi jumlah pemakaian."""
    while True:
        try:
            pemakaian = int(input("Masukkan jumlah pemakaian air (m³): "))
            if pemakaian >= 0:
                return pemakaian
            print("Pemakaian harus >= 0.")
        except ValueError:
            print("Input tidak valid. Masukkan angka.")

def main():
    """Fungsi utama program."""
    print("\n" + "="*50)
    print("PROGRAM HITUNG BIAYA RETRIBUSI AIR MINUM")
    print("Perusahaan Daerah Air Minum (PDAM)")
    print("="*50)
    
    while True:
        try:
            n = int(input("\nMasukkan jumlah pelanggan yang akan diproses: "))
            if n <= 0:
                print("Jumlah pelanggan harus lebih dari 0. Silakan coba lagi.")
                continue
            
            total_biaya = 0
            for i in range(n):
                print(f"\n[Pelanggan ke-{i + 1}]")
                kode = code()
                pemakaian = jumlah()
                
                tarif = uang(kode, pemakaian)
                biaya = hitung(pemakaian, tarif)
                total_biaya += biaya
                
                total(kode, pemakaian, tarif, biaya)
            
            # Tampilkan ringkasan
            print("\n" + "="*50)
            print("RINGKASAN HASIL PEMROSESAN")
            print("="*50)
            print(f"Total Pelanggan      : {n}")
            print(f"Total Biaya Seluruh  : Rp {total_biaya:,}")
            print(f"Rata-rata Biaya      : Rp {total_biaya // n:,}")
            print("="*50)
            break
            
        except ValueError:
            print("Input tidak valid. Masukkan angka untuk jumlah pelanggan.")
        except KeyboardInterrupt:
            print("\n\nProgram dihentikan pengguna.")
            break

if __name__ == '__main__':
    main()
