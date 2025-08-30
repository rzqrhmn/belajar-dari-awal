import matplotlib.pyplot as plt

# Data sederhana
hari = ["Senin", "Selasa", "Rabu", "Kamis", "Jumat"]
nilai = [70, 80, 75, 90, 85]

# Bikin grafik garis
plt.plot(hari, nilai)

# Kasih judul & label
plt.title("Nilai Belajar Mingguan")
plt.xlabel("Hari")
plt.ylabel("Nilai")

# Tampilkan grafik
plt.show()
