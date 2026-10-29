print("Mulai")
while True:    #This simulates a Do Loop
    print("---------------")
    print("Masukkan minat jurusan (IPA / IPS / Bahasa): ")
    minat = input()
    while minat != "ipa" and minat != "IPA" and minat != "ips" and minat != "IPS" and minat != "bahasa" and minat != "Bahasa":
        print("Minat tidak dikenali. Harus IPA / IPS / Bahasa.")
        print("Masukkan minat jurusan (IPA / IPS / Bahasa): ")
        minat = input()
    print("Masukkan nilai Matematika: ")
    mtk = int(input())
    print("Masukkan nilai Biologi: ")
    bio = int(input())
    print("Masukkan nilai Fisika: ")
    fis = int(input())
    print("Masukkan nilai Kimia: ")
    kim = int(input())
    print("Masukkan nilai Geografi: ")
    geo = int(input())
    print("Masukkan nilai Ekonomi: ")
    eko = int(input())
    print("Masukkan nilai Sosiologi: ")
    sos = int(input())
    print("Masukkan nilai Bahasa Indonesia: ")
    indo = int(input())
    print("Masukkan nilai Bahasa Inggris: ")
    ing = int(input())
    print("Masukkan nilai Bahasa Lain: ")
    lain = int(input())
    iPAlulus = mtk >= 80 and bio >= 78 and fis >= 78 and kim >= 78
    iPSlulus = mtk >= 80 and geo >= 78 and eko >= 80 and sos >= 78
    bHSlulus = mtk >= 75 and indo >= 80 and ing >= 78 and lain >= 75
    if minat == "IPA" or minat == "ipa":
        if iPAlulus == True:
            hasil = "Diterima di jurusan IPA"
        else:
            if iPSlulus == True:
                hasil = "Disarankan jurusan IPS"
            else:
                if bHSlulus == True:
                    hasil = "Disarankan jurusan Bahasa"
                else:
                    hasil = "Belum memenuhi syarat jurusan manapun"
    else:
        if minat == "IPS" or minat == "ips":
            if iPSlulus == True:
                hasil = "Diterima di jurusan IPS"
            else:
                if iPAlulus == True:
                    hasil = "Disarankan jurusan IPA"
                else:
                    if bHSlulus == True:
                        hasil = "Disarankan jurusan Bahasa"
                    else:
                        hasil = "Belum memenuhi syarat jurusan manapun"
        else:
            if bHSlulus == True:
                hasil = "Diterima di jurusan Bahasa"
            else:
                if iPAlulus == True:
                    hasil = "Disarankan jurusan IPA"
                else:
                    if iPSlulus == True:
                        hasil = "Disarankan jurusan IPS"
                    else:
                        hasil = "Belum memenuhi syarat jurusan manapun"
    print("Hasil penjurusan adalah: ")
    print(hasil)
    print("---------------")
    print("Ulangi?")
    print("Input n untuk berhenti")
    ulang = input()
    if ulang == "n" or ulang == "N" or ulang == "no" or ulang == "No": break
print("Selesai")

