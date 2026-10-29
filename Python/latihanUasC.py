def get_rates_by_category(cat):
    """Return (daily_rate, extra_hour_rate) for category 1/2/3.
    
    Args:
        cat (int): Kategori gedung (1, 2, 3)
    
    Returns:
        tuple: (daily_rate, extra_hour_rate) atau (None, None) jika kategori tidak valid
    """
    if cat == 1:
        return 300_000, 50_000
    if cat == 2:
        return 450_000, 80_000
    if cat == 3:
        return 600_000, 100_000
    return None, None


def calculate_charge(days, daily_rate, extra_hours, extra_rate):
    """Menghitung biaya sewa gedung dengan diskon jika lama sewa > 3 hari."""
    base = days * daily_rate
    extra = extra_hours * extra_rate
    subtotal = base + extra
    discount = 0
    if days > 3:
        discount = 0.1 * subtotal
    total = subtotal - discount
    return {
        'base': base,
        'extra': extra,
        'subtotal': subtotal,
        'discount': discount,
        'total': total,
    }


def read_int(prompt, min_value=None):
    """Membaca dan memvalidasi integer dengan nilai minimum opsional."""
    while True:
        s = input(prompt).strip()
        try:
            v = int(s)
        except ValueError:
            print("Input tidak valid. Masukkan angka bulat.")
            continue
        if min_value is not None and v < min_value:
            print(f"Masukkan angka >= {min_value}.")
            continue
        return v


def read_positive_int(prompt):
    """Membaca dan memvalidasi integer positif (>0)."""
    while True:
        try:
            v = int(input(prompt).strip())
            if v > 0:
                return v
            print("Masukkan angka lebih besar dari 0.")
        except ValueError:
            print("Input tidak valid. Masukkan angka bulat.")


def read_valid_category():
    """Membaca dan memvalidasi kategori gedung (1/2/3)."""
    while True:
        cat = read_int("Masukkan kategori gedung (1/2/3): ", min_value=1)
        if cat in (1, 2, 3):
            return cat
        print("Kategori tidak valid. Pilih 1, 2, atau 3.")


def display_cost_info(cat, days, extra_hours, daily_rate, extra_rate, charges):
    """Menampilkan rincian biaya dengan format yang rapi."""
    kategori_nama = {1: 'Gedung Pertemuan', 2: 'Gedung Pentas Seni', 3: 'Gedung Pernikahan'}
    print("\n" + "="*50)
    print("HASIL PERHITUNGAN BIAYA SEWA GEDUNG")
    print("="*50)
    print(f"Kategori Gedung     : {kategori_nama.get(cat, cat)}")
    print(f"Harga per hari      : Rp{daily_rate:,}")
    print(f"Harga per jam lebih : Rp{extra_rate:,}")
    print(f"Lama sewa (hari)    : {days}")
    print(f"Kelebihan jam       : {extra_hours}")
    print(f"Biaya sewa dasar    : Rp{charges['base']:,}")
    print(f"Biaya kelebihan jam : Rp{charges['extra']:,}")
    print(f"Subtotal            : Rp{int(charges['subtotal']):,}")
    print(f"Potongan (10% jika >3 hari): Rp{int(charges['discount']):,}")
    print(f"Total yang harus dibayar    : Rp{int(charges['total']):,}")
    print("="*50)


def main():
    """Fungsi utama program."""
    print("\n" + "="*50)
    print("PROGRAM KALKULATOR BIAYA SEWA GEDUNG")
    print("Perhitungan berdasarkan kategori dan lama sewa")
    print("="*50)

    print("\nKategori:\n 1) Gedung Pertemuan (Rp300.000/hari, Rp50.000/jam lebih)\n 2) Gedung Pentas Seni (Rp450.000/hari, Rp80.000/jam lebih)\n 3) Gedung Pernikahan (Rp600.000/hari, Rp100.000/jam lebih)")

    try:
        n = read_positive_int("\nMasukkan jumlah pelanggan yang akan diproses: ")
        total_biaya_keseluruhan = 0

        for i in range(1, n + 1):
            print(f"\n[Pelanggan ke-{i}]")
            cat = read_valid_category()
            days = read_int("Masukkan lama sewa (hari): ", min_value=1)
            extra_hours = read_int("Masukkan kelebihan jam (jam, 0 jika tidak ada): ", min_value=0)

            daily_rate, extra_rate = get_rates_by_category(cat)
            charges = calculate_charge(days, daily_rate, extra_hours, extra_rate)
            total_biaya_keseluruhan += charges['total']

            display_cost_info(cat, days, extra_hours, daily_rate, extra_rate, charges)

        # Tampilkan ringkasan
        print("\n" + "="*50)
        print("RINGKASAN HASIL PEMROSESAN")
        print("="*50)
        print(f"Total Pelanggan      : {n}")
        print(f"Total Biaya Seluruh  : Rp {int(total_biaya_keseluruhan):,}")
        print(f"Rata-rata Biaya      : Rp {int(total_biaya_keseluruhan) // n:,}")
        print("="*50)
        print("Terima kasih telah menggunakan layanan kami.")

    except KeyboardInterrupt:
        print("\n\nProgram dihentikan pengguna.")


if __name__ == '__main__':
    main()
