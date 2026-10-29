# Soal 1
# data = [3, 7, 11, 5, 12, 6, 16, 9]

# def bubblesort(data):
#     for i in range(len(data)):
#         for j in range(0, len(data) - i - 1):
#             if data[j] > data[j + 1]:
#                 temp = data[j]
#                 data[j] = data[j + 1]
#                 data[j + 1] = temp

# print("Bubble Sort")
# bubblesort(data)

# def bubblesortoptimized(data):
#     for i in range(len(data)):
#         swapped = False
#         for j in range(0, len(data) - i - 1):
#             if data[j] > data[j + 1]:
#                 temp = data[j]
#                 data[j] = data[j + 1]
#                 data[j + 1] = temp
#                 swapped = True
#         if swapped == False:
#             break

# print("Bubble Sort Optimized")
# bubblesortoptimized(data)

# print(data)

# Soal 2
# data = [1, 0.5, 5, 3, 2.6, 10.3, 1.7, 4.1]

# def selectionsort(data, size):
#     for i in range(size):
#         nilaiterbesar = i

#         for j in range(i + 1, size):
#             if data[j] > data[nilaiterbesar]:
#                 nilaiterbesar = j

#         temp = data[i]
#         data[i] = data[nilaiterbesar]
#         data[nilaiterbesar] = temp

# print("Selection Sort")
# selectionsort(data, 8)

# print(data)

# Soal 3
# def insertionsort(data):
#     for i in range(1, len(data)):
#         temp = data[i]
#         j = i - 1

#         while j >= 0 and temp.lower() < data[j].lower():
#             data[j + 1] = data[j]
#             j -= 1

#         data[j + 1] = temp

# kalimat = ("nusantara")
# huruf = [kalimat for kalimat in kalimat if kalimat.isalpha()]
# insertionsort(huruf)

# print("Kalimat awal: ", kalimat)
# print("Hasil akhir: ", "".join(huruf))

# Soal 1
# arr = [3, 7, 11, 5, 12, 6, 16, 9]
# def partisi(array, kiri, kanan):
#     pivot = array[kanan]
#     i = kiri - 1

#     for j in range(kiri, kanan):
#         if array[j] >= pivot:
#             i += 1
#             temp = array[i]
#             array[i] = array[j]
#             array[j] = temp

#     temp = array[i + 1]
#     array[i + 1] = array[kanan]
#     array[kanan] = temp
#     return i + 1

# def quicksort(array, kiri, kanan):
#     if kiri < kanan:
#         pi = partisi(array, kiri, kanan)
#         quicksort(array, kiri, pi - 1)
#         quicksort(array, pi + 1, kanan)

# quicksort(arr, 0, len(arr) - 1)
# print("Quick Sort")
# print(arr)

# Soal 2
# arr = [1, 0.5, 5, 3, 2.6, 10.3, 1.7, 4.1]

# def mergesort(array):
#     if len(array) > 1:
#         tengah = len(array) // 2
#         kiri = array[:tengah]
#         kanan = array[tengah:]

#         mergesort(kiri)
#         mergesort(kanan)
#         i = j = k = 0

#         while i < len(kiri) and j < len(kanan):
#             if kiri[i] <= kanan[j]:
#                 array[k] = kiri[i]
#                 i += 1
#             else:
#                 array[k] = kiri[j]
#                 j += 1
#             k += 1

#         while i < len(kiri):
#             array[k] = kiri[i]
#             i += 1
#             k += 1

#         while j < len(kanan):
#             array[k] = kanan[j]
#             j += 1
#             k += 1

# mergesort(arr)
# print("Merge Sort")
# print(arr)

# Soal 3
def shellsort(array, n):
    interval = n // 2
    while interval > 0:
        for i in range(interval, n):
            temp = array[i]
            j = i
            while j >= interval and array[j - interval].lower() > temp.lower():
                array[j] = array[j - interval]
                j -= interval
            array[j] = temp
        interval //= 2

kalimat = ("nusantara")
huruf = [kalimat for kalimat in kalimat if kalimat.isalpha()]
shellsort(huruf, len(huruf))

print("Kalimat awal: ", kalimat)
print("Hasil akhir: ", "".join(huruf))
