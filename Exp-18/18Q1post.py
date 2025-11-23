import matplotlib
matplotlib.use("TkAgg")   # Force GUI backend so graph will show

import librosa
import numpy as np
import matplotlib.pyplot as plt

# Load audio files
x, rate_x = librosa.load("input_audio.wav", sr=None)
h, rate_h = librosa.load("impulse_response.wav", sr=None)

print("Audio loaded:", x.shape)
print("Impulse loaded:", h.shape)

# Linear Convolution
y_linear = np.convolve(x, h)

# Circular Convolution
N = len(x) + len(h) - 1
y_circular = np.fft.ifft(np.fft.fft(x, N) * np.fft.fft(h, N)).real

# Plot
plt.figure(figsize=(10, 6))

plt.subplot(3, 1, 1)
plt.title("Input Audio")
plt.plot(x)

plt.subplot(3, 1, 2)
plt.title("Linear Convolution")
plt.plot(y_linear)

plt.subplot(3, 1, 3)
plt.title("Circular Convolution")
plt.plot(y_circular)

plt.tight_layout()
plt.show(block=True)
