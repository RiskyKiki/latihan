# Program konversi suhu menggunakan tuple dan tuple unpacking.
# Tuple menyimpan dua fungsi konversi dari Celsius: ke Fahrenheit dan ke Kelvin.
konversi = (
    lambda c: (c * 9/5) + 32,     # °C -> °F
    lambda c: c + 273.15          # °C -> K
)

# Unpack tuple ke dua variabel fungsi terpisah.
to_fahrenheit, to_kelvin = konversi

def main():
    print("=== KONVERSI SUHU (Tuple) ===")
    try:
        celsius = float(input("Masukkan suhu dalam Celsius: "))
    except ValueError:
        print("Input tidak valid. Masukkan angka untuk suhu.")
        return

    # Panggil fungsi konversi untuk nilai Celsius yang dimasukkan.
    fahrenheit = to_fahrenheit(celsius)
    kelvin = to_kelvin(celsius)

    # Tampilkan hasil konversi ke Fahrenheit dan Kelvin.
    print(f"\n{celsius:.2f}°C adalah:")
    print(f"- {fahrenheit:.2f}°F")
    print(f"- {kelvin:.2f} K")
    print("")


main()