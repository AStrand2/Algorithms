


import time
import random

def linear_search(lst, target):
    for i in range(len(lst)):
        if lst[i] == target:
            return i
    return -1

def binary_search(lst, target):
    low = 0
    high = len(lst) - 1
    while low <= high:
        mid = (low + high) // 2
        if lst[mid] == target:
            return mid
        elif lst[mid] < target:
            low = mid + 1
        else:
            high = mid - 1
    return -1

def bubble_sort(lst):
    n = len(lst)
    for i in range(n):
        for j in range(0, n-i-1):
            if lst[j] > lst[j+1]:
                lst[j], lst[j+1] = lst[j+1], lst[j]

def merge_sort(lst):
    if len(lst) > 1:
        mid = len(lst) // 2
        left_half = lst[:mid]
        right_half = lst[mid:]
        merge_sort(left_half)
        merge_sort(right_half)
        i = j = k = 0
        while i < len(left_half) and j < len(right_half):
            if left_half[i] < right_half[j]:
                lst[k] = left_half[i]
                i += 1
            else:
                lst[k] = right_half[j]
                j += 1
            k += 1
        while i < len(left_half):
            lst[k] = left_half[i]
            i += 1
            k += 1
        while j < len(right_half):
            lst[k] = right_half[j]
            j += 1
            k += 1

# create a list of random numbers to use in tests
lst = [random.randint(1, 1000) for _ in range(10000)]
target = random.choice(lst)

# measure the time it takes to perform each algorithm
start_time = time.time()
linear_search(lst, target)
end_time = time.time()
linear_search_time = end_time - start_time

start_time = time.time()
binary_search(lst, target)
end_time = time.time()
binary_search_time = end_time - start_time

start_time = time.time()
bubble_sort(lst)
end_time = time.time()
bubble_sort_time = end_time - start_time

start_time = time.time()
merge_sort(lst)
end_time = time.time()
merge_sort_time = end_time - start_time

# print the results
print("Linear search time:", linear_search_time)
print("Binary search time:", binary_search_time)
print("Bubble sort time:", bubble_sort_time)
print("Merge sort time:", merge_sort_time)
