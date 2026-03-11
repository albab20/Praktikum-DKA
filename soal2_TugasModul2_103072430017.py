import numpy as np

namaBarang = []
kodeBarang = []
jumlah = []
hargaPerUnit = []

n = int(input("Masukkan jumlah barang: "))

for i in range(n):
    print("Data Barang ke-", i+1)
    namaBarang.append(input("Nama Barang: "))
    kodeBarang.append(input("Kode Barang: "))
    jumlah.append(int(input("Jumlah: ")))
    hargaPerUnit.append(float(input("Harga Per Unit: ")))

namaBarang = np.array(namaBarang)
kodeBarang = np.array(kodeBarang)
jumlah = np.array(jumlah)
hargaPerUnit = np.array(hargaPerUnit)

print("\nData Inventaris:")
for i in range(n):
    print(namaBarang[i], kodeBarang[i], jumlah[i], hargaPerUnit[i])

print("\nTotal Nilai Inventaris:")
for i in range(n):
    total = jumlah[i] * hargaPerUnit[i]
    print(namaBarang[i], ":", total)

cari = input("\nMasukkan Nama Barang atau Kode Barang yang dicari: ")

for i in range(n):
    if cari == namaBarang[i] or cari == kodeBarang[i]:
        print("Data Barang:")
        print("Nama Barang:", namaBarang[i])
        print("Kode Barang:", kodeBarang[i])
        print("Jumlah:", jumlah[i])
        print("Harga Per Unit:", hargaPerUnit[i])