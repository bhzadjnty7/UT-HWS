import numpy as np
from pypuf.simulation import ArbiterPUF
n_stages = 64
num_crps = 10000 # Number of challenge-response pairs to generate
puf = ArbiterPUF(n=n_stages)
# Generate random binary challenges .
challenges = np.random.randint(0, 2, size=(num_crps, n_stages))
responses = puf.eval(challenges)
# Save challenges and responses to CSV files .
np.savetxt("challenges.csv", challenges, fmt="%d", delimiter=",")
np.savetxt("responses.csv", responses, fmt="%d", delimiter=",")
print(f"Generated {num_crps} CRPs — files 'challenges.csv' and 'responses.csv' saved.")