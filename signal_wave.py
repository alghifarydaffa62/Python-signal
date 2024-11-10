import numpy as np
import matplotlib.pyplot as plt

# Parameter Gelombang
amplitude = 1     # Amplitudo gelombang
frequency = 1     # Frekuensi dalam Hertz
time = np.linspace(0, 2, 500)  # Waktu dalam detik (0 hingga 2 detik, 500 titik data)

sine_wave = amplitude * np.sin(2 * np.pi * frequency * time)

plt.figure(figsize=(10, 5))
plt.plot(time, sine_wave, label='Gelombang Sinusoidal')
plt.title("Visualisasi Gelombang Sinusoidal")
plt.xlabel("Waktu (detik)")
plt.ylabel("Amplitudo")
plt.legend()
plt.grid(True)
plt.show()
