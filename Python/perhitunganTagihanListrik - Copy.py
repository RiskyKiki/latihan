# Program Perhitungan Tagihan Listrik

# Input nama pelanggan
nama = str(input("Masukkan nama pelanggan: "))

# Input pemakaian listrik dengan validasi loop - Menangani input tidak wajar
while True:
    try:
        pemakaian_listirik = int(input("Masukkan jumlah pemakaian listrik (dalam kWh): "))
        # Validasi: pemakaian tidak boleh negatif
        if pemakaian_listirik < 0:
            print("Pemakaian listrik tidak boleh negatif! Silakan input ulang.")
            continue
        break  # Input valid, keluar dari loop
    except ValueError:
        # Menangani input yang bukan angka
        print("Input harus berupa angka! Silakan input ulang.")

# Input jenis rumah dengan validasi loop - Menangani input tidak wajar
while True:
    jenis_rumah = str(input("Masukkan jenis rumah (subsidi/nonsubsidi): ")).lower()
    # Validasi: jenis rumah harus subsidi atau nonsubsidi
    if jenis_rumah == "subsidi" or jenis_rumah == "nonsubsidi":
        break  # Input valid, keluar dari loop
    else:
        print("Jenis rumah hanya bisa 'subsidi' atau 'nonsubsidi'! Silakan input ulang.")

# Ketentuan:
# - Tarif berbeda tergantung jenis rumah
# - Pemakaian tinggi akan dikenakan biaya tambahan
# - Dalam kondisi tertentu, pelanggan bisa mendapatkan potongan harga
# - Sistem harus menangani kemungkinan nilai input tidak wajar

# Nested IF: Cek jenis rumah (subsidi/nonsubsidi) menggunakan if-elif-else
if jenis_rumah == "subsidi":
    tarif_per_kwh = 605  # Tarif rumah subsidi
    # Nested IF: Cek range pemakaian untuk menentukan kategori biaya
    if pemakaian_listirik >= 300:
        # Jika pemakaian tinggi (>=300 kWh), tambah biaya 25%
        biaya_akhir = pemakaian_listirik * tarif_per_kwh * 1.25
        keterangan = "tambahan biaya"
    elif pemakaian_listirik <= 100:
        # Jika pemakaian rendah (<=100 kWh), diskon 10%
        biaya_akhir = pemakaian_listirik * tarif_per_kwh * 0.9
        keterangan = "diskon"
    else:
        # Jika pemakaian normal (101-299 kWh)
        biaya_akhir = pemakaian_listirik * tarif_per_kwh
        keterangan = "normal"

elif jenis_rumah == "nonsubsidi":
    tarif_per_kwh = 1352  # Tarif rumah nonsubsidi
    # Nested IF: Sama seperti subsidi, tapi tarif berbeda
    if pemakaian_listirik >= 300:
        biaya_akhir = pemakaian_listirik * tarif_per_kwh * 1.25
        keterangan = "tambahan biaya"
    elif pemakaian_listirik <= 100:
        biaya_akhir = pemakaian_listirik * tarif_per_kwh * 0.9
        keterangan = "diskon"
    else:
        biaya_akhir = pemakaian_listirik * tarif_per_kwh
        keterangan = "normal"

else:
    # Jika input jenis rumah tidak valid
    print("Jenis rumah tidak valid. Harap masukkan 'subsidi' atau 'nonsubsidi'.")

# Output hasil
print("\nTotal tagihan listrik untuk pelanggan", nama)
print("Jumlah pemakaian listrik:", pemakaian_listirik, "kWh")
print("Keterangan:", keterangan)
