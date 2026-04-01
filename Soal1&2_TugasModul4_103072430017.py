import matplotlib.pyplot as plt

data = [
    ("Budi", 81.24, 73.66, 95.89, 2023),
    ("Siti", 98.52, 84.86, 88.7, 2024),
    ("Asep", 91.96, 71.03, 79.93, 2022),
    ("Dewi", 87.96, 97.28, 71.91, 2024),
    ("Andi", 74.68, 77.76, 79.33, 2023),
    ("Lestari", 74.68, 89.88, 79.76, 2022),
    ("Joko", 71.74, 79.35, 91.89, 2022),
    ("Rina", 95.99, 85.6, 89.13, 2022),
    ("Fajar", 88.03, 86.4, 96.62, 2024),
    ("Indah", 91.24, 75.55, 84.17, 2023),
    ("Agus", 70.62, 99.09, 73.59, 2022),
    ("Fitri", 99.1, 93.25, 91.4, 2022),
    ("Rudi", 94.97, 98.18, 92.82, 2022),
    ("Maya", 76.37, 96.84, 86.84, 2024),
    ("Hadi", 75.45, 87.94, 93.13, 2024),
    ("Sri", 75.5, 97.66, 84.81, 2023),
    ("Wawan", 79.13, 72.65, 85.68, 2024),
    ("Yuni", 85.74, 75.88, 82.83, 2022),
    ("Bambang", 82.96, 71.36, 70.76, 2023),
    ("Ayu", 78.74, 79.76, 73.24, 2022),
]

a2022 = [[], [], []]
a2023 = [[], [], []]
a2024 = [[], [], []]

for d in data:
    n1 = d[1]
    n2 = d[2]
    n3 = d[3]
    tahun = d[4]

    if tahun == 2022:
        a2022[0].append(n1)
        a2022[1].append(n2)
        a2022[2].append(n3)
    elif tahun == 2023:
        a2023[0].append(n1)
        a2023[1].append(n2)
        a2023[2].append(n3)
    elif tahun == 2024:
        a2024[0].append(n1)
        a2024[1].append(n2)
        a2024[2].append(n3)

fig, axes = plt.subplots(2, 2, figsize=(10, 8))
axes = axes.flatten()

matkul = ["Algoritma", "Matdis", "AI"]

semua = [a2022, a2023, a2024]
tahun_list = [2022, 2023, 2024]

for i in range(3):
    ax = axes[i]
    nilai_matkul = semua[i]

    ax.boxplot(nilai_matkul)

    print("\nAngkatan", tahun_list[i])

    for j in range(3):
        mk = nilai_matkul[j]

        total = 0
        for x in mk:
            total = total + x
        mean = total / len(mk)

        min_val = min(mk)
        max_val = max(mk)

        print(matkul[j], "-> mean:", round(mean,2),
              "min:", round(min_val,2),
              "max:", round(max_val,2))

        posisi = j + 1

        ax.scatter(posisi, mean)
        ax.scatter(posisi, min_val)
        ax.scatter(posisi, max_val)

        ax.text(posisi, mean, str(round(mean,1)), ha='center', fontsize=6)
        ax.text(posisi, min_val, str(round(min_val,1)), ha='center', fontsize=6)
        ax.text(posisi, max_val, str(round(max_val,1)), ha='center', fontsize=6)

    ax.set_title("Angkatan " + str(tahun_list[i]))
    ax.set_xticklabels(matkul)
    ax.set_ylim(50, 100)

axes[3].axis('off')

plt.tight_layout()
plt.show()