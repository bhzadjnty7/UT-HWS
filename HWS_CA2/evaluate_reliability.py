import numpy as np
from pypuf.simulation import ArbiterPUF
from sklearn.metrics import pairwise_distances
n_stages = 64
num_crps = 1000 # Use a subset for faster computation
puf = ArbiterPUF(n=n_stages)
#Generate challenges .
challenges = np.random.randint(0, 2, size=(num_crps, n_stages))
#Evaluate the same challenge set twice .
responses1 = puf.eval(challenges)
responses2 = puf.eval(challenges)
#Calculate Hamming distances (as a fraction) .
distances = np.mean(responses1 != responses2)
print("Average intra-chip Hamming distance:", distances)
