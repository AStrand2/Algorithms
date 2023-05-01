
def knapsack_backtracking(values, weights, limit):
    def backtrack(i, weight):
        if i < 0:
            return 0
        elif weights[i] > weight:
            return backtrack(i - 1, weight)
        else:
            return max(backtrack(i - 1, weight), values[i] + backtrack(i - 1, weight - weights[i]))
    
    return backtrack(len(values) - 1, limit)

def knapsack_dynamic(values, weights, limit):
    n = len(values)
    dp = [[0 for _ in range(limit + 1)] for _ in range(n + 1)]
    
    for i in range(1, n + 1):
        for w in range(1, limit + 1):
            if weights[i - 1] <= w:
                dp[i][w] = max(dp[i - 1][w], values[i - 1] + dp[i - 1][w - weights[i - 1]])
            else:
                dp[i][w] = dp[i - 1][w]
                
    return dp[n][limit]

import random
import time

# generate random instances of the Knapsack Problem
def generate_instances(num_instances, max_items, max_weight):
    instances = []
    for i in range(num_instances):
        n = random.randint(1, max_items)
        limit = random.randint(1, max_weight)
        values = [random.randint(1, 100) for _ in range(n)]
        weights = [random.randint(1, limit) for _ in range(n)]
        instances.append((values, weights, limit))
    return instances

# measure the run time of each algorithm for each instance
def measure_time(algorithm, instances):
    times = []
    for instance in instances:
        start_time = time.time()
        algorithm(*instance)
        end_time = time.time()
        times.append(end_time - start_time)
    return times


instances = generate_instances(10, 120, 300)
backtracking_times = measure_time(knapsack_backtracking, instances)
dynamic_times = measure_time(knapsack_dynamic, instances)

for i in range(len(instances)):
    print(f"Instance {i+1}: Backtracking Time = {backtracking_times[i]:.6f} s, Dynamic Time = {dynamic_times[i]:.6f} s")


