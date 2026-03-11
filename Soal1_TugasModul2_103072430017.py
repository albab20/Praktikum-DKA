import numpy as np

nama = []
nim = []
nilai = []
tahunMasuk = []

n = int(input("Masukkan jumlah mahasiswa: "))

for i in range(n):
    print("Data Mahasiswa ke-", i+1)
    nama.append(input("Nama: "))
    nim.append(input("NIM: "))
    nilai.append(float(input("Nilai: ")))
    tahunMasuk.append(int(input("Tahun Masuk: ")))

nama = np.array(nama)
nim = np.array(nim)
nilai = np.array(nilai)
tahunMasuk = np.array(tahunMasuk)

print("\nData Mahasiswa:")
for i in range(n):
    print(nama[i], nim[i], nilai[i], tahunMasuk[i])

print("\nNilai Tertinggi:", np.max(nilai))
print("Nilai Terendah:", np.min(nilai))
print("Nilai Rata-rata:", np.mean(nilai))

cari = input("\nMasukkan Nama atau NIM yang dicari: ")

for i in range(n):
    if cari == nama[i] or cari == nim[i]:
        print("Data Mahasiswa:")
        print("Nama:", nama[i])
        print("NIM:", nim[i])
        print("Nilai:", nilai[i])
        print("Tahun Masuk:", tahunMasuk[i])