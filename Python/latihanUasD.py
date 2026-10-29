def get_rate(category, year):
    """
    Mendapatkan tarif sewa berdasarkan kategori dan tahun.
    
    Args:
        category (str): Kategori gudang ('A', 'B', 'C')
        year (int): Tahun ke- (1 untuk tahun pertama, >1 untuk tahun berikutnya)
    
    Returns:
        int: Tarif sewa per tahun atau None jika kategori tidak valid
    """
    category = category.upper()
    if category == 'A':
        if year == 1:
            return 6000000
        else:
            return 5000000
    if category == 'B':
        if year == 1:
            return 5000000
        else:
            return 4000000
    if category == 'C':
        if year == 1:
            return 5500000
        else:
            return 5000000
    return None


def calculate_total_cost(category, years):
    """
    Menghitung total biaya sewa gudang untuk kategori dan jumlah tahun tertentu.
    
    Args:
        category (str): Kategori gudang
        years (int): Jumlah tahun sewa
    
    Returns:
        int: Total biaya sewa
    """
    total = 0
    for year in range(1, years + 1):
        rate = get_rate(category, year)
        total += rate
    return total


def read_valid_category():
    """Membaca dan memvalidasi input kategori gudang (A/B/C)."""
    while True:
        category = input("Masukkan kategori gudang (A=Elektronik, B=Bangunan, C=Mebeler): ").strip()
        if get_rate(category, 1) is not None:
            return category.upper()
        print("Kategori tidak valid. Masukkan A, B, atau C.")


def read_positive_int(prompt):
    """Membaca dan memvalidasi input integer positif (>0)."""
    while True:
        s = input(prompt).strip()
        try:
            v = int(s)
            if v > 0:
                return v
            print("Masukkan angka bulat lebih besar dari 0.")
        except ValueError:
            print("Input tidak valid. Masukkan angka bulat.")


def display_cost_info(name, category, years, total_cost):
    """Menampilkan rincian biaya sewa gudang dengan format yang rapi."""
    kategori_nama = {'A': 'Elektronik', 'B': 'Bangunan', 'C': 'Mebeler'}
    print("\n" + "="*50)
    print("HASIL PERHITUNGAN BIAYA SEWA GUDANG")
    print("="*50)
    print(f"Nama Penyewa        : {name}")
    print(f"Kategori Gudang     : {kategori_nama.get(category, category)}")
    print(f"Lama Sewa (Tahun)   : {years}")
    print(f"Total Biaya Sewa    : Rp {total_cost:,}")
    print("="*50)


def main():
    """Fungsi utama program."""
    print("\n" + "="*50)
    print("PROGRAM HITUNG BIAYA SEWA GUDANG")
    print("Komplek Pergudangan - Perhitungan Biaya Tahunan")
    print("="*50)
    
    try:
        n = read_positive_int("\nMasukkan jumlah penyewa yang akan diproses: ")
        total_biaya_keseluruhan = 0

        for i in range(1, n + 1):
            print(f"\n[Penyewa ke-{i}]")
            name = input("Masukkan nama penyewa: ").strip()
            if not name:
                print("Nama tidak boleh kosong. Lewati penyewa ini.")
                continue
            
            category = read_valid_category()
            years = read_positive_int("Masukkan lama sewa (tahun): ")

            total_cost = calculate_total_cost(category, years)
            total_biaya_keseluruhan += total_cost

            display_cost_info(name, category, years, total_cost)

        # Tampilkan ringkasan
        print("\n" + "="*50)
        print("RINGKASAN HASIL PEMROSESAN")
        print("="*50)
        print(f"Total Penyewa        : {n}")
        print(f"Total Biaya Seluruh  : Rp {int(total_biaya_keseluruhan):,}")
        print(f"Rata-rata Biaya      : Rp {int(total_biaya_keseluruhan) // n:,}")
        print("="*50)
        print("Terima kasih telah menggunakan layanan kami.")

    except KeyboardInterrupt:
        print("\n\nProgram dihentikan pengguna.")


if __name__ == '__main__':
    main()
