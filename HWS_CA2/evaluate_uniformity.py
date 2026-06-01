from pypuf.simulation import ArbiterPUF
from pypuf.metrics import bias

bias(ArbiterPUF(n=64, seed=42), seed=1)

