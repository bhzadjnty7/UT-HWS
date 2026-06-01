import numpy as np
from pypuf.simulation import XORArbiterPUF
from pypuf.metrics import bias

# تنظیم پارامترها
n_stages = 64
n_xors = 4
seed = 2

# ساخت PUF
puf = XORArbiterPUF(n=n_stages, k=n_xors, seed=seed)

# محاسبه bias
bias_value = bias(puf, seed=seed)  # درست: اعمال بر روی شی PUF نه پاسخ‌ها
uniformity = 1 - abs(bias_value)

print("XOR PUF - Bias:", bias_value)
print("XOR PUF - Uniformity:", uniformity)

bias(XORArbiterPUF(n=64, k=2, seed=2), seed=2)
