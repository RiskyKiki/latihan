import math

# Menggunakan nested tuple untuk menyimpan koordinat titik-titik.
titik = (
    (2, 3),  # Titik A
    (5, 7),  # Titik B
    (1, 4)   # Titik C
) 

def jarak(A, B):
    # x1, y1 = A
    # x2, y2 = B
    # return ((x2 - x1) ** 2 + (y2 - y1) ** 2) ** 0.5
    return math.dist(A, B)  
    # Menggunakan math.dist untuk menghitung jarak antara dua titik


def luas_segitiga(A, B, C):
    x1, y1 = A
    x2, y2 = B
    x3, y3 = C
    return abs((x1*(y2 - y3) + x2*(y3 - y1) + x3*(y1 - y2)) / 2)
    # Menggunakan rumus Shoelace
    # abs digunakan untuk memastikan luas selalu positif
    # karena rumus ini bisa menghasilkan nilai negatif tergantung pada urutan titik.

def main():
    A, B, C = titik  # Unpack tuple ke variabel A, B, C

    print("Titik A:", A)
    print("Titik B:", B)
    print("Titik C:", C)  

    # Hitung jarak antara titik A dan B
    jarak_AB = jarak(A, B)
    print(f"Jarak antara A dan B: {jarak_AB:.2f}")

    # Hitung luas segitiga yang dibentuk oleh titik A, B, dan C
    luas_ABC = luas_segitiga(A, B, C)
    print(f"Luas segitiga ABC: {luas_ABC:.2f}")

main()