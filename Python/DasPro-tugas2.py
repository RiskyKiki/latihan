# Bilangan genap atau ganjil
bilangan = int(input("Masukkan bilangan: "))

if bilangan % 2 == 0:
    print("Bilangan Genap")
else:
    print("Bilangan Ganjil")

# Tahun kabisat
tahun = int(input("Masukkan tahun: "))

if (tahun % 400 == 0) or (tahun % 4 == 0 and tahun % 100 != 0):
    print("Tahun kabisat")
else:
    print("Bukan tahun kabisat")

# Kalkulator sederhana
bilangan1 = float(input("Masukkan angka pertama: "))
bilangan2 = float(input("Masukkan angka kedua: "))
operator = input("Masukkan operator (+, -, *, /): ")

if operator == '+':
    hasil = bilangan1 + bilangan2
    print("Hasil =", hasil)

elif operator == '-':
    hasil = bilangan1 - bilangan2
    print("Hasil =", hasil)

elif operator == '*':
    hasil = bilangan1 * bilangan2
    print("Hasil =", hasil)

elif operator == '/':
    if bilangan2 != 0:
        hasil = bilangan1 / bilangan2
        print("Hasil =", hasil)
    else:
        print("Error: Tidak bisa dibagi nol!")

else:
    print("Operator tidak valid!")