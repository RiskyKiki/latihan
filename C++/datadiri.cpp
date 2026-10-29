#include <iostream>
#include <string>
#include <sstream>
#include <iomanip>

// Utility: read a line of text (trim leading/trailing newlines handled by getline)
static std::string read_line(const std::string &prompt) {
	std::string s;
	std::cout << prompt;
	std::getline(std::cin, s);
	return s;
}

// Utility: read integer with validation by reading a line and parsing
static int read_int(const std::string &prompt) {
	while (true) {
		std::string line = read_line(prompt);
		std::istringstream iss(line);
		int v;
		if (iss >> v) return v;
		std::cout << "Input tidak valid. Silakan masukkan angka bulat.\n";
	}
}

// Utility: read double with validation
static double read_double(const std::string &prompt) {
	while (true) {
		std::string line = read_line(prompt);
		std::istringstream iss(line);
		double v;
		if (iss >> v) return v;
		std::cout << "Input tidak valid. Silakan masukkan angka (contoh: 123.45).\n";
	}
}

int main() {
	// Make sure we start with a clean input state
	std::cout << "Program Data Diri\n";
	std::cout << "-------------------\n";

	std::string nama = read_line("Masukkan nama: ");
	std::string jenis_kelamin = read_line("Masukkan jenis kelamin: ");
	int usia = read_int("Masukkan usia (tahun): ");
	std::string sekolah = read_line("Masukkan sekolah saat ini: ");
	std::string asal_sekolah = read_line("Masukkan asal sekolah (sebelumnya): ");
	double nilai_akhir = read_double("Masukkan nilai akhir rapot (angka): ");
	double uang_saku = read_double("Masukkan uang saku (per bulan, angka): ");
	double uang_saku_mingguan = read_double("Masukkan uang saku mingguan (angka): ");
	double uang_tabungan = read_double("Masukkan jumlah uang tabungan (angka): ");

	std::cout << "\n=== Ringkasan Data Diri ===\n";
	std::cout << "Nama               : " << nama << '\n';
	std::cout << "Jenis kelamin      : " << jenis_kelamin << '\n';
	std::cout << "Usia               : " << usia << " tahun\n";
	std::cout << "Sekolah            : " << sekolah << '\n';
	std::cout << "Asal sekolah       : " << asal_sekolah << '\n';
	std::cout << std::fixed << std::setprecision(2);
	std::cout << "Nilai akhir rapot  : " << nilai_akhir << '\n';
	std::cout << "Uang saku (bulan)  : " << uang_saku << '\n';
	std::cout << "Uang saku (minggu) : " << uang_saku_mingguan << '\n';
	std::cout << "Uang tabungan      : " << uang_tabungan << '\n';

	return 0;
}

