angka = int(input(("Masukan angka: ")))

if angka % 2 == 0:
    print(f"{angka} adalah bilangan genap")
else:
    print(f"{angka} adalah bilangan ganjil")
print(f"{angka} adalah bilangan {'genap' if angka % 2 == 0 else 'ganjil'}")

