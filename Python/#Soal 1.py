#Soal 1
# import array as a

# arr = a.array("i", [12, 5, 21, 2, 8, 15])

# panjang = 0
# total = 0

# for a in arr:
#     panjang += 1
#     total += a

# rata = total / panjang

# print(f"Panjang array: {panjang}")
# print(f"Total nilai array: {total}")
# print(f"Rata-rata array: {rata}")


#Soal 2
# import array as a

# arr = a.array("i", [12, 8, 100, -45, 3, -1])

# minimal = min(arr)
# maksimal = max(arr)

# print(f"Nilai minimal: {minimal}")
# print(f"Nilai maksimal: {maksimal}")


#Soal 3
# import numpy as np

# arr1 = np.array([[2,3],[8,1]])
# arr2 = np.array([[6,5],[7,9]])

# pengurangan = arr1 - arr2

# print("Hasil Pengurangan Matriks:")
# for baris in pengurangan:
#     print(f"[{baris[0]} {baris[1]}]")


#Soal 4
# import numpy as np

# arr1 = np.array([[2,4,3],[3,2,8],[1,4,7]])
# arr2 = np.array([[1,5,2],[8,12,4],[11,6,6]])

# perkalian = np.dot(arr1, arr2)

# print("Hasil Perkalian Matriks:")
# for baris in perkalian:
#     print(f"[{baris[0]} {baris[1]} {baris[2]}]")


#Soal 5
import numpy as np

arr = np.array([[1,4,3],[7,5,8],[9,2,3]])

angka = int(input("Masukkan angka yang ingin dicari:"))

for i in range(len(arr)):
    for j in range(len(arr[i])):
        if arr[i][j] == angka:
            print(f"Baris: {i + 1}, Kolom: {j + 1}")
            break
    else:
        continue
    break
else:
    print(f"Angka {angka} tidak ditemukan")

