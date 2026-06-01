import numpy as np
from pypuf.simulation import XORArbiterPUF

n_stages = 64
num_xors = 4  # تعداد XORهای ترکیبی
num_crps = 10000

# ساخت PUF
puf = XORArbiterPUF(n=n_stages, k=num_xors)

# تولید چالش‌ها و پاسخ‌ها
challenges = np.random.randint(0, 2, size=(num_crps, n_stages))
responses = puf.eval(challenges)

# ذخیره در فایل
np.savetxt("xor_challenges.csv", challenges, fmt="%d", delimiter=",")
np.savetxt("xor_responses.csv", responses, fmt="%d", delimiter=",")
print("Generated", num_crps, "XOR CRPs.")
