from pypuf.simulation import ArbiterPUF
# Instantiate an Arbiter PUF with 64 stages
n_stages = 64
puf = ArbiterPUF(n=n_stages)
print("Arbiter PUF instantiated with", n_stages, "stages.")