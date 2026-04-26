import pandas as pd
import random
from rocket_simulator import simulate

data = []

for i in range(400):
    mass = random.uniform(0.5, 5.0)
    thrust = random.uniform(20, 100)
    burn_time = random.uniform(1, 5)

    height = simulate(mass, thrust, burn_time)

    data.append([mass, thrust, burn_time, height])

df = pd.DataFrame(data, columns=["mass", "thrust", "burn_time", "max_height"])

df.to_csv("rocket_data.csv", index=False)

print("Dataset created!")