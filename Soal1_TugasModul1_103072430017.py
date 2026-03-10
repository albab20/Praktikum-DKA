def isKabisat(tahun):
    if (tahun % 4 == 0 and tahun % 100 != 0) or (tahun % 400 == 0):
        return True
    else:
        return False

# Memanggil fungsi dan memeriksa hasilnya
tahun_input = int(input("Masukkan tahun: "))

hasil = isKabisat(tahun_input)

if hasil:
    print(tahun_input, "adalah tahun kabisat")
else:
    print(tahun_input, "bukan tahun kabisat")