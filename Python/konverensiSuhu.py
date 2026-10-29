# fungsi untuk mengubah celsius ke fahrenheit
def cel_to_fah(c):
    return (c * 9/5) + 32

# fungsi untuk mengubah fahrenheit ke celsius
def fah_to_cel(f):
    return (f - 32) * 5/9

# procedure untuk menampilkan hasil konversi suhu
def hasil(suhu, satuan):
    # jika celsius, ubah ke fahrenheit
    if satuan.upper() == 'C':
        # panggil fungsi konversi
        result = cel_to_fah(suhu)
        print(f"{suhu}°C = {result:.2f}°F")
    # jika fahrenheit, ubah ke celsius
    elif satuan.upper() == 'F':
        # panggil fungsi konversi
        result = fah_to_cel(suhu)
        print(f"{suhu}°F = {result:.2f}°C")
    # jika tidak valid
    else:
        print("Satuan tidak valid (C/F)")

# main program
suhu = float(input("Masukkan nilai suhu: "))
satuan = input("Pilih satuan (C/F): ")
# panggil procedure
hasil(suhu, satuan)
