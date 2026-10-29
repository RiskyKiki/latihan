alas = float(input("Masukan alas: "))
tinggi = float(input("Masukan tinggi: "))

luas = 0.5 * alas * tinggi

print("Luas segitiga adalah:",luas)
print(f"Luas segitiga adalah: {luas}")
print(f"Luas segitiga adalah: {luas:.2f}")
print("Luas segitiga adalah: %.2f" % luas)
print("Luas segitiga adalah: {:.2f}".format(luas))
print(f"0.5 x {alas} x {tinggi} = {luas}")


