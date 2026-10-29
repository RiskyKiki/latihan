def biaya_tambahan(total_hours, rate_per_hour):
    if total_hours <= 1:
        return 0
    return (total_hours - 1) * rate_per_hour

def hasil(jam_parkir, biaya_jam_pertama, biaya_jam_selanjutnya):
    
    tambahan = biaya_tambahan(jam_parkir, biaya_jam_selanjutnya)
    total = biaya_jam_pertama + tambahan

    print("========================================")
    print(f"Biaya parkir untuk 1 jam pertama adalah {biaya_jam_pertama}")

    if jam_parkir > 1:
        print(f"Biaya parkir untuk jam selanjutnya adalah {tambahan}")
        
    print(f"Total biaya parkir adalah {total}")
    print("========================================")

def main():
    while True:
        print("Menghitung biaya parkir roda empat")
        print("Pilih jenis kendaraan:")
        print("1. Sedan")
        print("2. Minibus/Minivan")
        print("3. Bus/Truck")

        while True:
            val = input("Masukkan pilihan (1/2/3): ")
            try:
                jenis = int(val)
            except ValueError:
                print("Input tidak valid. Masukkan angka 1, 2, atau 3.")
                continue
            if jenis in (1, 2, 3):
                break
            print("Pilihan tidak valid. Masukkan 1, 2, atau 3.")

        if jenis == 1:
            biaya_jam_pertama = 5000
            biaya_jam_selanjutnya = 3000
        elif jenis == 2:
            biaya_jam_pertama = 7000
            biaya_jam_selanjutnya = 3500
        elif jenis == 3:
            biaya_jam_pertama = 6000
            biaya_jam_selanjutnya = 2500

        while True:
            val = input("Masukkan lama parkir (dalam jam): ")
            try:
                jam_parkir = int(val)
            except ValueError:
                print("Input tidak valid. Masukkan angka untuk lama jam.")
                continue
            if jam_parkir > 0:
                break
            print("Lama parkir tidak valid. Masukkan angka lebih besar dari 0.")

        hasil(jam_parkir, biaya_jam_pertama, biaya_jam_selanjutnya)

        while True:
            lagi = input("Ingin selesai atau jalankan lagi? (y = selesai, n = ulang): ").strip().lower()
            if lagi in ("y", "yes"):
                print("Program selesai. Terima kasih.")
                return
            if lagi in ("n", "no"):
                print("Menjalankan ulang...")
                print("========================================")
                break
            print("Input tidak dikenal. Ketik 'y' untuk selesai atau 'n' untuk ulang.")

if __name__ == "__main__":
    main()