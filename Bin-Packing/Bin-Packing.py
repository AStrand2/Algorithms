import random
import time
import math


def first_fit(items, bin_capacity):
    # Initialize a list of bins, with the first bin initially empty
    bins = [bin_capacity]
    
    # Iterate through each item and place it in the first bin it fits in
    for item in items:
        placed = False
        for i in range(len(bins)):
            if bins[i] >= item:
                bins[i] -= item
                placed = True
                break
        if not placed:
            bins.append(bin_capacity - item)
    
    # Return the number of bins used
    return len(bins)



def simulated_annealing(items, bin_capacity, initial_temp=1000, cooling_rate=0.003, stopping_temp=1e-8, stopping_iter=1000):
    # Initialize a random solution
    solution = [random.randint(0, i) for i in range(len(items))]
    num_bins = max(solution) + 1
    
    # Calculate the initial cost (number of bins used)
    cost = num_bins
    
    # Initialize the temperature and iteration count
    temperature = initial_temp
    iter_count = 0
    
    while temperature > stopping_temp and iter_count < stopping_iter:
        # Choose a neighboring solution
        neighbor = list(solution)
        i = random.randint(0, len(items) - 1)
        j = random.randint(0, len(items) - 1)
        neighbor[i] = random.randint(0, max(solution))
        neighbor[j] = random.randint(0, max(solution))
        
        # Calculate the cost of the neighboring solution
        neighbor_num_bins = max(neighbor) + 1
        
        # If the neighboring solution is better, accept it
        if neighbor_num_bins < num_bins:
            solution = neighbor
            num_bins = neighbor_num_bins
            cost = num_bins
        # If the neighboring solution is worse, accept it with a probability proportional to the temperature
        else:
            delta = neighbor_num_bins - num_bins
            accept_prob = math.exp(-delta / temperature)
            if random.random() < accept_prob:
                solution = neighbor
                num_bins = neighbor_num_bins
                cost = num_bins
        
        # Decrease the temperature and increase the iteration count
        temperature *= 1 - cooling_rate
        iter_count += 1
    
    return cost


# Define the bin capacity and number of items to generate
bin_capacity = 10
num_items = 10000

# Define a function to generate a random list of items
def generate_items():
    return [random.randint(1, bin_capacity) for i in range(num_items)]

# Run the First-Fit Algorithm 10 times and measure the time it takes to complete
first_fit_times = []
for i in range(10):
    items = generate_items()
    
    start_time = time.time()
    first_fit(items, bin_capacity)
    end_time = time.time()
    first_fit_times.append(end_time - start_time)

# Run the Simulated Annealing Algorithm 10 times and measure the time it takes to complete
simulated_annealing_times = []
for i in range(10):
    items = generate_items()
    
    start_time = time.time()
    simulated_annealing(items, bin_capacity)
    end_time = time.time()
    simulated_annealing_times.append(end_time - start_time)

# Compute the average time for each algorithm
avg_first_fit_time = sum(first_fit_times) / len(first_fit_times)
avg_simulated_annealing_time = sum(simulated_annealing_times) / len(simulated_annealing_times)

# Print the average time for each algorithm
print(f"First-Fit Algorithm: Average time = {avg_first_fit_time:.4f} seconds")
print(f"Simulated Annealing Algorithm: Average time = {avg_simulated_annealing_time:.4f} seconds")
