import random
import time


def merge_sort(array):
    """
    Sorts the given array in ascending order using the merge sort algorithm.
    """
    if len(array) > 1:
        mid = len(array) // 2
        left_half = array[:mid]
        right_half = array[mid:]
        merge_sort(left_half)
        merge_sort(right_half)
        i = j = k = 0
        while i < len(left_half) and j < len(right_half):
            if left_half[i] < right_half[j]:
                array[k] = left_half[i]
                i += 1
            else:
                array[k] = right_half[j]
                j += 1
            k += 1
        while i < len(left_half):
            array[k] = left_half[i]
            i += 1
            k += 1
        while j < len(right_half):
            array[k] = right_half[j]
            j += 1
            k += 1


def quick_sort(array):
    if len(array) <= 1:
        return array
    stack = [(0, len(array) - 1)]
    while stack:
        left, right = stack.pop()
        if left >= right:
            continue
        pivot = array[left]
        i, j = left, right
        while i < j:
            while i < j and array[j] >= pivot:
                j -= 1
            array[i] = array[j]
            while i < j and array[i] <= pivot:
                i += 1
            array[j] = array[i]
        array[i] = pivot
        stack.append((left, i - 1))
        stack.append((i + 1, right))
    return array


def measure_time(algorithm, array):
    start_time = time.time()
    sorted_array = run_sorting_algorithm(algorithm, array)
    end_time = time.time()
    return end_time - start_time


def run_sorting_algorithm(algorithm, array):
    """
    Runs the specified sorting algorithm on the given array and prints the sorted and unsorted arrays.
    """
    #print("Unsorted array:", array)
    start_time = time.time()
    if algorithm == "mergesort":
        merge_sort(array)
    elif algorithm == "quicksort":
        array = quick_sort(array)
    end_time = time.time()
    #print("Sorted array:", array)
    print(f"Time taken for {algorithm}: {end_time - start_time:.6f}s")
    return end_time - start_time


def run_fixture(algorithm1, algorithm2, array_size, num_iterations):
    """
    Runs the specified sorting algorithms on arrays of the given size for the specified number of iterations and prints the
    average time taken by each algorithm.
    """
    total_time1 = total_time2 = 0
    for i in range(num_iterations):
        array = [random.randint(0, 1000) for _ in range(array_size)]
        total_time1 += measure_time(algorithm1, array)
        total_time2 += measure_time(algorithm2, array)
    print(f"Average time taken for {algorithm1}: {total_time1/num_iterations:.6f}s")
    print(f"Average time taken for {algorithm2}: {total_time2/num_iterations:.6f}s")


if __name__ == "__main__":
    array_size = 10000
    num_iterations = 10
    run_fixture("mergesort", "quicksort", array_size, num_iterations)
