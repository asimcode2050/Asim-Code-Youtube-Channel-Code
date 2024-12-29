import numpy as np
import matplotlib.pyplot as plt
sampling_rate = 1000 
square_wave_frequency = 50 
T = 1
N = sampling_rate * T
t = np.linspace(0, T, N, endpoint=False)
square_wave = np.sign(np.sin(2 * np.pi * square_wave_frequency * t))
plt.figure(figsize=(10, 4))
plt.plot(t, square_wave)
plt.title("Square Wave Signal")
plt.xlabel("Time [s]")
plt.ylabel("Amplitude")
plt.grid(True)
plt.show()
fft_result = np.fft.fft(square_wave)
frequencies = np.fft.fftfreq(N, 1/sampling_rate)
fft_magnitude = np.abs(fft_result)
half_n = N // 2
frequencies = frequencies[:half_n]
fft_magnitude = fft_magnitude[:half_n]
plt.figure(figsize=(10, 4))
plt.plot(frequencies, fft_magnitude)
plt.title("FFT of the Square Wave")
plt.xlabel("Frequency [Hz]")
plt.ylabel("Magnitude")
plt.grid(True)
plt.show()

