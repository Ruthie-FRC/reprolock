from reprolock.rng_guard import set_seed
from reprolock.verify import hash_output, check_output
import random

# Step 1: control all randomness
set_seed(42)

# Step 2: tiny simulation
positions = [random.randint(0, 100) for _ in range(5)]
velocities = [random.randint(1, 10) for _ in range(5)]

print("Positions:", positions)
print("Velocities:", velocities)

# Step 3: simple update
for i in range(5):
    positions[i] += velocities[i]

print("Updated positions:", positions)

# Step 4: hash and verify
simulation_data = {
    "positions": positions,
    "velocities": velocities
}

# first time running, generate baseline hash
# baseline_hash = hash_output(simulation_data)
# print("Baseline hash:", baseline_hash)

# replace this number with the hash from the first run
# baseline_hash = "your_baseline_hash_here"
baseline_hash = "930082ecfa5f3ca2b9e160805ad6adc0462c2a944befd29d60ab443e8b558090"
