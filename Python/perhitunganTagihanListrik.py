# Program Perhitungan Tagihan Listrik

# Input nama pelanggan
nama = str(input("Masukkan nama pelanggan: "))
    
# Input pemakaian listrik dengan loop validasi
while True:
    try:
        pemakaian_listirik = int(input("Masukkan jumlah pemakaian listrik (dalam kWh): "))
        if pemakaian_listirik < 0:
            print("Pemakaian listrik tidak boleh negatif! Silakan input ulang.")
            continue
        break  # Input valid, keluar loop
    except ValueError:
        print("Input tidak valid! Pastikan pemakaian listrik berupa angka. Silakan input ulang.")

# Input jenis rumah dengan loop validasi
while True:
    jenis_rumah = str(input("Masukkan jenis rumah (subsidi/non-subsidi): ")).lower()
    if jenis_rumah in ["subsidi", "non-subsidi"]:
        break  # Input valid, keluar loop
    else:
        print("Jenis rumah tidak valid! Harap masukkan 'subsidi' atau 'non-subsidi'. Silakan input ulang.")

# Ketentuan:
# - Tarif berbeda tergantung jenis rumah
# - Pemakaian tinggi akan dikenakan biaya tambahan
# - Dalam kondisi tertentu, pelanggan bisa mendapatkan potongan harga
# - Sistem harus menangani kemungkinan nilai input tidak wajar

# Hitung biaya dengan nested if
if jenis_rumah == "subsidi":
    tarif_per_kwh = 605
    if pemakaian_listirik >= 300:
        biaya_akhir = pemakaian_listirik * tarif_per_kwh * 1.25  # Tambah 25%
        keterangan = "tambahan biaya"
    elif pemakaian_listirik <= 100:
        biaya_akhir = pemakaian_listirik * tarif_per_kwh * 0.9   # Diskon 10%
        keterangan = "diskon"
    else:
        biaya_akhir = pemakaian_listirik * tarif_per_kwh
        keterangan = "normal"

elif jenis_rumah == "non-subsidi":
    tarif_per_kwh = 1352
    if pemakaian_listirik >= 300:
        biaya_akhir = pemakaian_listirik * tarif_per_kwh * 1.25  # Tambah 25%
        keterangan = "tambahan biaya"
    elif pemakaian_listirik <= 100:
        biaya_akhir = pemakaian_listirik * tarif_per_kwh * 0.9   # Diskon 10%
        keterangan = "diskon"
    else:
        biaya_akhir = pemakaian_listirik * tarif_per_kwh
        keterangan = "normal"

else:
    print("Jenis rumah tidak valid. Harap masukkan 'subsidi' atau 'non-subsidi'.")
    exit()

# Output hasil
print("Total tagihan listrik untuk pelanggan", nama)
print("Jumlah pemakaian listrik:", pemakaian_listirik, "kWh")
print("Keterangan:", keterangan)
