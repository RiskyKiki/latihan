def hitung_hari(hari,inputhari,):
    return hari * inputhari

def hitung_jam(jam, inputjam):
    return jam * inputjam

def main():
    while True:
        gedung = int(input("masukkan kategori gedung (1/2/3): "))    
        if gedung == 1:
            hari = 300000
            jam = 50000
        elif gedung == 2:
            hari = 45000
            jam = 80000
        elif gedung == 3:
            hari = 600000
            jam = 100000
        else:
            print("Input salah")
            continue

    while True:
        hari = int(input("Masukkan hari sewa:"))
        if hari > 0:
            jam = int(input("Masukkan jam berlebih:"))
        print("Input salah")
        continue

main()