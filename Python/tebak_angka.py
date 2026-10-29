import random  #Mengimpor modul random untuk menghasilkan angka acak

def tebak_angka():  #Fungsi utama untuk permainan tebak angka
    rahasia = random.randint(1, 50) #Menghasilkan angka rahasia antara 1 dan 50
    percobaan = 0  # Variabel untuk menghitung jumlah percobaan

    # Loop utama permainan tebak angka
    while True:
        # Meminta input tebakan dari pengguna dan mengubah ke integer
        tebak = int(input("Tebak angka: "))
        percobaan += 1 #jumlah awal percobaan

        # Mengecek apakah tebakan benar
        if tebak == rahasia:
            print("Benar!")
            break
        # Jika tebakan salah
        elif tebak < rahasia:
            print("Terlalu kecil")
        else:
            print("Terlalu besar")

        # jika percobaan mencapai 10 kali maka akan muncul opsi menyerah
        if percobaan >= 10:
            nyerah = input("Anda sudah mencoba 10 kali. Ingin menyerah? (y/n): ")
            #.lower() untuk merubah input menjadi huruf kecil
            if nyerah.lower() == "y": 
                print(f"Angka rahasia adalah {rahasia}")
                break

# Pesan selamat datang
print("Game Tebak Angka")
jumlah_bermain = 0
# Loop untuk memungkinkan bermain lagi
while True:
    tebak_angka()
    jumlah_bermain += 1
    lagi = input("Ingin bermain lagi? (y/n): ")
    if lagi.lower() != "y": 
        print("Terima kasih telah bermain!")
        print(f"Jumlah permainan: {jumlah_bermain}")
        break
