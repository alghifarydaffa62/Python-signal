import numpy as np
import matplotlib.pyplot as plt

# Parameter sinyal
frequency = 5  # frekuensi sinyal analog (Hz)
sampling_rate = 50  # laju sampling untuk sinyal digital
time = np.linspace(0, 1, 1000)  # rentang waktu untuk sinyal analog

# Membuat sinyal analog (gelombang sinusoidal)
analog_signal = np.sin(2 * np.pi * frequency * time)

# Membuat sinyal digital (diskretisasi sinyal analog)
digital_time = np.linspace(0, 1, sampling_rate, endpoint=False)  # diskretisasi waktu
digital_signal = np.sign(np.sin(2 * np.pi * frequency * digital_time))  # sinyal digital dengan nilai -1 atau 1

# Plotting sinyal
plt.figure(figsize=(12, 6))

# Plot sinyal analog
plt.subplot(2, 1, 1)
plt.plot(time, analog_signal, label="Analog Signal (Sine Wave)", color="blue")
plt.title("Analog Signal")
plt.xlabel("Time (s)")
plt.ylabel("Amplitude")
plt.grid(True)
plt.legend()

# Plot sinyal digital
plt.subplot(2, 1, 2)
plt.step(digital_time, digital_signal, where="post", label="Digital Signal", color="red")
plt.title("Digital Signal")
plt.xlabel("Time (s)")
plt.ylabel("Amplitude")
plt.grid(True)
plt.legend()

# Menampilkan plot
plt.tight_layout()
plt.show()
