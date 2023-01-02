import numpy as np
import matplotlib.pyplot as plt

# Set the number of iterations and the initial population size
num_iterations = 200
pop_size = 0.5

# Set the range of the control parameter r
r_min = 2.5
r_max = 4.0
num_points = 1000

# Create an array of control parameter values
r_values = np.linspace(r_min, r_max, num_points)

# Initialize an array to store the population sizes at each iteration
pop_sizes = np.empty((num_points, num_iterations))

# Iterate over the control parameter values
for i, r in enumerate(r_values):
    # Set the initial population size
    pop_sizes[i, 0] = pop_size
    # Iterate over the remaining iterations
    for j in range(1, num_iterations):
        pop_sizes[i, j] = r * pop_sizes[i, j - 1] * (1 - pop_sizes[i, j - 1])

# Plot the bifurcation diagram
plt.plot(r_values, pop_sizes, ',k', alpha=0.1)
plt.show()
