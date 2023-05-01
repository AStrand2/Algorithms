import time

# Divide and conquer algorithm
def binomial_coefficient_dc(n, k):
    #print("Called binomial_coefficient_dc with n =", n, "and k =", k)
    if k == 0 or k == n:
        return 1
    return binomial_coefficient_dc(n-1, k-1) + binomial_coefficient_dc(n-1, k)

# Dynamic programming algorithm
def binomial_coefficient_dp(n, k):
    #print("Called binomial_coefficient_dp with n =", n, "and k =", k)
    table = [[0 for j in range(k+1)] for i in range(n+1)]
    for i in range(n+1):
        table[i][0] = 1
    for i in range(1, n+1):
        for j in range(1, min(i+1, k+1)):
            table[i][j] = table[i-1][j-1] + table[i-1][j]
    return table[n][k]


#Defining the variables for the algorithms
n = 30
k = 15

# Using divide and conquer algorithm
start_time = time.time()
result_dc = binomial_coefficient_dc(n, k)
end_time = time.time()
time_dc = end_time - start_time

# Using dynamic programming algorithm
start_time = time.time()
result_dp = binomial_coefficient_dp(n, k)
end_time = time.time()
time_dp = end_time - start_time

print(f"Divide and conquer algorithm result: {result_dc}, time: {time_dc}")
print(f"Dynamic programming algorithm result: {result_dp}, time: {time_dp}")
