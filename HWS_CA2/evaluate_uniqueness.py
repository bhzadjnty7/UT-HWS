import numpy as np
from pypuf.simulation import ArbiterPUF
n_stages = 64
num_crps = 1000
#Create two distinct PUF instances .
puf1 = ArbiterPUF(n=n_stages, seed=1)
puf2 = ArbiterPUF(n=n_stages, seed=2)
challenges = np.random.randint(0, 2, size=(num_crps, n_stages))
responses1 = puf1.eval(challenges)
responses2 = puf2.eval(challenges)
#Compute average Hamming distance between responses of the two PUFs .
uniqueness = np.mean(responses1 != responses2)
print("Average inter-chip Hamming distance:", uniqueness)