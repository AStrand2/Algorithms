
def knapsack_dp(values, weights, W):
    n = len(values)
    dp = [[0 for j in range(W+1)] for i in range(n+1)]
    
    for i in range(1, n+1):
        for j in range(1, W+1):
            if weights[i-1] > j:
                dp[i][j] = dp[i-1][j]
            else:
                dp[i][j] = max(dp[i-1][j], dp[i-1][j-weights[i-1]] + values[i-1])
    
    return dp[n][W]

def knapsack_greedy(values, weights, W):
    n = len(values)
    items = list(zip(values, weights))
    items.sort(key=lambda x: x[0]/x[1], reverse=True)
    
    total_value = 0
    for value, weight in items:
        if W >= weight:
            total_value += value
            W -= weight
        else:
            total_value += (W/weight) * value
            break
    
    return total_value

import random
import time

# Generate inputs
n = 1000
W = 1000
values = [random.randint(1, 100) for i in range(n)]
weights = [random.randint(1, 100) for i in range(n)]

# Test both algorithms
n_trials = 10
dp_times = []
greedy_times = []
for i in range(n_trials):
    start_time = time.time()
    knapsack_dp(values, weights, W)
    dp_time = time.time() - start_time
    dp_times.append(dp_time)
    
    start_time = time.time()
    knapsack_greedy(values, weights, W)
    greedy_time = time.time() - start_time
    greedy_times.append(greedy_time)

# Print average run times
print("DP average time: ", sum(dp_times)/n_trials)
print("Greedy average time: ", sum(greedy_times)/n_trials)
