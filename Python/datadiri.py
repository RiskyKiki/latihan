def read_nonempty(prompt):
    while True:
        s = input(prompt).strip()
        if s:
            return s
        print("Input tidak boleh kosong. Coba lagi.")


def read_int(prompt):
    while True:
        s = input(prompt).strip()
        try:
            return int(s)
        except ValueError:
            print("Input tidak valid. Masukkan angka bulat (contoh: 17).")


def read_float(prompt):
    while True:
        s = input(prompt).strip()
        try:
            return float(s)
        except ValueError:
            print("Input tidak valid. Masukkan angka (contoh: 87.5).")


if __name__ == '__main__':
    print("Program Input Data Diri")
    print("-----------------------")
    nama = read_nonempty("Nama: ")
    jenis_kelamin = read_nonempty("Jenis kelamin: ")
    usia = read_int("Usia (tahun): ")
    sekolah = read_nonempty("Sekolah saat ini: ")
    asal_sekolah = read_nonempty("Asal sekolah (sebelumnya): ")
    nilai_akhir = read_float("Nilai akhir rapot: ")
    uang_saku = read_float("Uang saku (per bulan): ")
    uang_saku_mingguan = read_float("Uang saku mingguan: ")
    uang_tabungan = read_float("Jumlah uang tabungan: ")

    print("\n=== Ringkasan Data Diri ===")
    print(f"Nama               : {nama}")
    print(f"Jenis kelamin      : {jenis_kelamin}")
    print(f"Usia               : {usia} tahun")
    print(f"Sekolah            : {sekolah}")
    print(f"Asal sekolah       : {asal_sekolah}")
    print(f"Nilai akhir rapot  : {nilai_akhir:.2f}")
    print(f"Uang saku (bulan)  : {uang_saku:.2f}")
    print(f"Uang saku (minggu) : {uang_saku_mingguan:.2f}")
    print(f"Uang tabungan      : {uang_tabungan:.2f}")
