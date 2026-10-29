nilaites = int(input("Masukkan nilai tes: "))

if 0 < nilaites < 100:
    print("Valid")
elif nilaites > 100:
    print("Nilai melebihi batas")
elif nilaites < 0:
    print("Invalid")
else:
    print("Nilai tidak boleh 0")
