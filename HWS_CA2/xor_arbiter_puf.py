from pypuf.simulation import XORArbiterPUF

n_stages = 64
k = 4 
puf = XORArbiterPUF(n=n_stages, k=k)
print(f"XOR Arbiter PUF instantiated with {n_stages} stages and {k} PUFs XORed together.")