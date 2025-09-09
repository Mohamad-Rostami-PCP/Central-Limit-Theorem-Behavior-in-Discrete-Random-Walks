from random import random
from statistics import pstdev
from statistics import mean
import numpy as np
from time import time
import matplotlib.pyplot as plt

# Variables
M = int(input("How many random walks you want us to create: "))
N = int(input("How many steps in each random walks you want us to make: "))
D = np.zeros((M + 1, N + 1))


# Functions
def move():
    random_val = random()
    if random_val < 0.5:
        return -1
    if random_val >= 0.5:
        return 1


time_s = time()
# Iterations

for i in range(M + 1):

    for j in range(N + 1):
        if j != 0:
            D[i][j] = D[i][j - 1] + move()

    # Statistics
    mean = np.zeros(N + 1, dtype=float)
    for k in range(N + 1):
        mean[k] = np.mean(D[:, k])

    variance = np.zeros(N+ 1, dtype=float)
    for k in range(N + 1):
        variance[k] = np.var(D[:, k])


# Running time calculation
time_e = time()
total_time = round(time_e - time_s, 2)

# Demonstrate result
print(f"Simulation and calculations took {total_time} seconds to run")

figure, axis = plt.subplots(2)

axis[0].plot(mean, 'o', ms=1)
axis[0].set_ylabel("Average(<x>)")
axis[0].set_ylim(-10, 10)

axis[1].plot(variance, 'o', ms=1)
axis[1].set_xlabel("Number of steps")
axis[1].set_ylabel("Variance(<x^2>)")

plt.show()
