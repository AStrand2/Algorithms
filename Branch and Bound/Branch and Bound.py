
import random
import heapq
import time

# Define the problem constraints
N = 20  # Number of items
W = 50  # Knapsack capacity
weights = [random.randint(1, 10) for i in range(N)]
values = [random.randint(1, 10) for i in range(N)]

# Define a function to compute the upper bound of the objective function
def upper_bound(capacity, remaining_items, values, weights):
    bound = sum(values[:remaining_items])
    for v, w in zip(values[remaining_items:], weights[remaining_items:]):
        if w <= capacity:
            bound += v
            capacity -= w
        else:
            bound += v * capacity / w
            break
    return bound

# Define a function to check if a node is feasible
def is_feasible(node, weights, capacity):
    return sum(weights[i] for i in range(node)) <= capacity

# Define a function to create the child nodes of a node
def create_children(node):
    return [node + 1, node + 1]

# Define a function to select the next variable to branch on
def select_variable(node, values, weights):
    return max(range(node, len(values)), key=lambda i: values[i] / weights[i])

# Define a function to update the current best solution
def update_best(node, values, weights, capacity, best_value, best_solution):
    if node == len(values):
        if best_value < sum(values[i] for i in best_solution):
            return sum(values[i] for i in range(node)), list(best_solution)
        else:
            return best_value, list(best_solution)
    else:
        return best_value, list(best_solution)

# Define the Depth-First Branch and Bound Algorithm
def dfs_bb(capacity, remaining_items, values, weights):
    stack = [(0, 0, [])]
    best_value, best_solution = 0, []
    while stack:
        node, value, solution = stack.pop()
        if value + upper_bound(capacity, remaining_items - node, values, weights) <= best_value:
            continue
        if is_feasible(node, weights, capacity):
            best_value, best_solution = update_best(node, values, weights, capacity, best_value, solution)
        if node < remaining_items:
            variable = select_variable(node, values, weights)
            for child in create_children(node):
                stack.append((child, value + values[variable] * child, solution + [variable]))
    return best_value, best_solution

# Define the Best-First Branch and Bound Algorithm
def best_first_bb(capacity, remaining_items, values, weights):
    queue = [(-upper_bound(capacity, remaining_items, values, weights), 0, 0, [])]
    best_value, best_solution = 0, []
    while queue:
        _, node, value, solution = heapq.heappop(queue)
        if value + upper_bound(capacity, remaining_items - node, values, weights) <= best_value:
            continue
        if is_feasible(node, weights, capacity):
            best_value, best_solution = update_best(node, values, weights, capacity, best_value, solution)
        if node < remaining_items:
            variable = select_variable(node, values, weights)
            for child in create_children(node):
                heapq.heappush(queue, (-upper_bound(capacity - child * weights[variable], remaining_items - node - child, values, weights), child, value + values[variable] * child, solution + [variable]))
    return best_value, best_solution

# Generate random data set
N = 20
W = 50
weights = [random.randint(1, 10) for i in range(N)]
values = [random.randint(1, 10) for i in range(N)]

# Run the Depth-First Branch and Bound Algorithm
start_time = time.time()
dfs_value, dfs_solution = dfs_bb(W, N, values, weights)
dfs_time = time.time() - start_time

# Run the Best-First Branch and Bound Algorithm
start_time = time.time()
bf_value, bf_solution = best_first_bb(W, N, values, weights)
bf_time = time.time() - start_time

# Print the results
print(f"Depth-First Branch and Bound Algorithm:\nValue: {dfs_value}\nSolution: {dfs_solution}\nTime: {dfs_time}")
print(f"Best-First Branch and Bound Algorithm:\nValue: {bf_value}\nSolution: {bf_solution}\nTime: {bf_time}")
