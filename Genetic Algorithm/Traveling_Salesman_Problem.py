import random

# Define the knapsack problem instance
capacity = 50
weights = [10, 20, 30, 40, 50, 60, 70, 80, 90, 100]
values = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10]

# Define the genetic algorithm parameters
population_size = 50
mutation_rate = 0.1
generations = 100

# Generate an initial population of candidate solutions
population = []
for i in range(population_size):
    solution = [random.randint(0, 1) for i in range(len(weights))]
    population.append(solution)

# Define the fitness function
def calculate_fitness(solution):
    total_value = 0
    total_weight = 0
    for i in range(len(solution)):
        if solution[i] == 1:
            total_value += values[i]
            total_weight += weights[i]
    if total_weight > capacity:
        return 0
    else:
        return total_value

# Apply the genetic algorithm
for i in range(generations):
    # Evaluate the fitness of each individual in the population
    fitness_values = [calculate_fitness(individual) for individual in population]
    
    # Select the fittest individuals for reproduction
    selected_indices = random.sample(range(population_size), 2)
    parent1 = population[selected_indices[0]]
    parent2 = population[selected_indices[1]]
    
    # Apply crossover to create a new child
    crossover_point = random.randint(0, len(weights) - 1)
    child = parent1[:crossover_point] + parent2[crossover_point:]
    
    # Apply mutation to the child
    for j in range(len(weights)):
        if random.random() < mutation_rate:
            child[j] = 1 - child[j]
    
    # Replace the least fit individual in the population with the child
    least_fit_index = fitness_values.index(min(fitness_values))
    population[least_fit_index] = child
    
# Find the best solution in the final population
fitness_values = [calculate_fitness(individual) for individual in population]
best_index = fitness_values.index(max(fitness_values))
best_individual = population[best_index]

# Print the best solution
print("Best solution:", best_individual)
print("Total value:", calculate_fitness(best_individual))
