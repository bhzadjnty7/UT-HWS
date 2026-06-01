import numpy as np
from pypuf.simulation import XORArbiterPUF

n_stages = 64
num_xors = 4
num_crps = 1000

puf1 = XORArbiterPUF(n=n_stages, k=num_xors, seed=1)
puf2 = XORArbiterPUF(n=n_stages, k=num_xors, seed=2)

challenges = np.random.randint(0, 2, size=(num_crps, n_stages))

responses1 = puf1.eval(challenges)
responses2 = puf2.eval(challenges)

uniqueness = np.mean(responses1 != responses2)

print("XOR PUF - Average inter-chip Hamming distance (Uniqueness):", uniqueness)
