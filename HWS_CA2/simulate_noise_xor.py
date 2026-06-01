import numpy as np
from pypuf.simulation import XORArbiterPUF
import matplotlib.pyplot as plt

n_stages = 64
num_xors = 4
num_crps = 1000
noise_level = 0.05  # 5% نویز

puf = XORArbiterPUF(n=n_stages, k=num_xors)

challenges = np.random.randint(0, 2, size=(num_crps, n_stages))
responses_clean = puf.eval(challenges)

# افزودن نویز
noise = np.random.rand(*responses_clean.shape) < noise_level
responses_noisy = np.bitwise_xor(responses_clean, noise.astype(int))

noise_effect = np.mean(responses_clean != responses_noisy)

print("XOR PUF - Noise-induced Hamming distance:", noise_effect)

plt.figure(figsize=(10, 3))
plt.plot(responses_clean[:50], 'b.-', label="Clean")
plt.plot(responses_noisy[:50], 'r.-', label="Noisy")
plt.legend()
plt.title("XOR PUF - Clean vs Noisy Responses (First 50 CRPs)")
plt.xlabel("Challenge Index")
plt.ylabel("Response Bit")
plt.show()
