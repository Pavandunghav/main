import random
import numpy as np
from deap import base, creator, tools, algorithms
import matplotlib.pyplot as plt

# Objective Function to Maximize
def objective(individual):
    x = individual[0]
    return x * np.sin(10 * np.pi * x) + 1,

# Create Fitness and Individual Classes
creator.create("FitnessMax", base.Fitness, weights=(1.0,))
creator.create("Individual", list, fitness=creator.FitnessMax)

# Set Up Toolbox
toolbox = base.Toolbox()
toolbox.register("attr_float", random.uniform, 0.0, 1.0)
toolbox.register("individual", tools.initRepeat, creator.Individual, toolbox.attr_float, n=1)
toolbox.register("population", tools.initRepeat, list, toolbox.individual)

toolbox.register("evaluate", objective)
toolbox.register("mate", tools.cxBlend, alpha=0.5)
toolbox.register("mutate", tools.mutGaussian, mu=0, sigma=0.1, indpb=0.1)
toolbox.register("select", tools.selTournament, tournsize=3)

# GA Parameters
population_size = 50
num_generations = 40
crossover_prob = 0.7
mutation_prob = 0.2

# Initialize Population
pop = toolbox.population(n=population_size)

# Statistics
stats = tools.Statistics(lambda ind: ind.fitness.values)
stats.register("avg", np.mean)
stats.register("max", np.max)

# Run Genetic Algorithm
pop, log = algorithms.eaSimple(pop, toolbox,
                               cxpb=crossover_prob,
                               mutpb=mutation_prob,
                               ngen=num_generations,
                               stats=stats,
                               verbose=True)

# Best Solution
best_ind = tools.selBest(pop, 1)[0]
print(f"\nBest Individual: {best_ind}, f(x) = {objective(best_ind)[0]:.5f}")

# Plotting the optimization curve
gen = log.select("gen")
maxs = log.select("max")
plt.plot(gen, maxs, label='Max Fitness')
plt.xlabel("Generation")
plt.ylabel("Fitness")
plt.title("DEAP Optimization Progress")
plt.legend()
plt.grid()
plt.show()
