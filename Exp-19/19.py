# import numpy as np
# from scipy.signal import TransferFunction

# # ---- Poles and Zeros ----
# num = [1, 0.5]              # Numerator coefficients
# den = [1, -1.5, 0.5]        # Denominator coefficients

# system = TransferFunction(num, den)

# print("Zeros:", system.zeros)
# print("Poles:", system.poles)


# import numpy as np
# from scipy.signal import TransferFunction

# # ---- Stability Check ----
# num = [1, 0.5]
# den = [1, -1.5, 0.5]

# system = TransferFunction(num, den)
# poles = system.poles

# stable = all(np.abs(p) < 1 for p in poles)

# print("Poles:", poles)
# print("Stability:", "Stable" if stable else "Unstable")

# # ---- Causality & Time Invariance ----
# num = [1, 0.5]

# # Causality: true for most LTI systems unless numerator degree > denominator
# causal = True  

# print("Causality:", "Causal" if causal else "Non-Causal")

# # Time Invariance:
# print("Time Invariance:", "Time Invariant")

import numpy as np
import matplotlib.pyplot as plt
from scipy.signal import TransferFunction, bode

# ---- Bode Plot ----
num = [1, 0.5]
den = [1, -1.5, 0.5]

system = TransferFunction(num, den)

w, mag, phase = bode(system)

plt.figure(figsize=(12, 8))

# Magnitude Plot
plt.subplot(2, 1, 1)
plt.semilogx(w, mag)
plt.title("Bode Magnitude Plot")
plt.xlabel("Frequency (rad/s)")
plt.ylabel("Magnitude (dB)")
plt.grid()

# Phase Plot
plt.subplot(2, 1, 2)
plt.semilogx(w, phase)
plt.title("Bode Phase Plot")
plt.xlabel("Frequency (rad/s)")
plt.ylabel("Phase (degrees)")
plt.grid()

plt.tight_layout()
plt.show()
