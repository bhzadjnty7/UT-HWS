import numpy as np
from pypuf.simulation import XORArbiterPUF

n_stages = 64
num_xors = 4
num_crps = 1000

puf = XORArbiterPUF(n=n_stages, k=num_xors)

challenges = np.random.randint(0, 2, size=(num_crps, n_stages))

responses1 = puf.eval(challenges)
responses2 = puf.eval(challenges)

reliability = np.mean(responses1 != responses2)

print("XOR PUF - Average intra-chip Hamming distance (Reliability):", reliability)
