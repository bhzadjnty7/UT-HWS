import numpy as np
from pypuf.simulation import ArbiterPUF
import matplotlib.pyplot as plt
n_stages = 64
num_crps = 1000
puf = ArbiterPUF(n=n_stages)
challenges = np.random.randint(0, 2, size=(num_crps, n_stages))
responses_clean = puf.eval(challenges)
#Introduce noise: flip bits with a given probability .
noise_level = 0.05 # 5% noise
noise = np.random.rand(*responses_clean.shape) < noise_level
responses_noisy = np.bitwise_xor(responses_clean, noise.astype(int))
#Calculate average Hamming distance between clean and noisy responses .
noise_effect = np.mean(responses_clean != responses_noisy)
print("Average Hamming distance due to noise:", noise_effect)
#Plot a small segment of clean vs noisy responses .
plt.figure(figsize=(10, 3))
plt.plot(responses_clean[:50], 'b.-', label="Clean")
plt.plot(responses_noisy[:50], 'r.-', label="Noisy")
plt.legend ()
plt.title("Comparison of Clean and Noisy Responses (First 50 CRPs)")
plt.xlabel("Challenge Index")
plt.ylabel("Response Bit")
plt.show()
