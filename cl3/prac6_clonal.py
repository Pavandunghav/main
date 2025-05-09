import numpy as np
import matplotlib.pyplot as plt

# Objective function to optimize
def objective_function(x):
    return x * np.sin(10 * np.pi * x) + 1.0

# Hyperparameters
population_size = 20
num_clones = 5
num_generations = 50
mutation_rate = 0.1
lower_bound = 0
upper_bound = 1

# Initialize population (antibodies)
population = np.random.uniform(lower_bound, upper_bound, population_size)

# Main Clonal Selection Algorithm loop
for gen in range(num_generations):
    # Evaluate affinity (fitness)
    fitness = objective_function(population)

    # Clone and mutate
    clones = []
    for i in np.argsort(-fitness):  # Sort descending by fitness
        parent = population[i]
        for _ in range(num_clones):
            clone = parent + np.random.normal(0, mutation_rate)
            clone = np.clip(clone, lower_bound, upper_bound)
            clones.append(clone)

    # Evaluate clones
    clones = np.array(clones)
    clone_fitness = objective_function(clones)

    # Select best individuals from clones and population
    combined = np.concatenate([population, clones])
    combined_fitness = np.concatenate([fitness, clone_fitness])
    best_indices = np.argsort(-combined_fitness)[:population_size]
    population = combined[best_indices]

    # Print best result in this generation
    best_solution = population[0]
    best_fitness = objective_function(best_solution)
    print(f"Generation {gen+1}: Best x = {best_solution:.4f}, f(x) = {best_fitness:.4f}")

# Plot final best solution
x_vals = np.linspace(0, 1, 1000)
y_vals = objective_function(x_vals)
plt.plot(x_vals, y_vals, label="f(x)")
plt.axvline(best_solution, color='r', linestyle='--', label='Best x')
plt.title("Clonal Selection Optimization")
plt.xlabel("x")
plt.ylabel("f(x)")
plt.legend()
plt.grid()
plt.show()
