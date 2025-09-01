import numpy as np
import matplotlib.pyplot as plt

# Buat data waktu dari 0 sampai 2π, sebanyak 1000 titik
t = np.linspace(0, 2*np.pi, 100)

# Rumus gelombang sinus
y = np.sin(t)

# Bikin grafik
plt.plot(t, y)

# Tambahkan judul dan label
plt.title("Gelombang Sinus Sederhana")
plt.xlabel("Waktu (s)")
plt.ylabel("Amplitudo")
plt.grid(True)

# Tampilkan grafik
plt.show()
