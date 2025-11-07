import random
import time

def quicksort(arr):
    if len(arr) <= 1:
        return arr
    
    pivot = arr[len(arr) // 2]
    left = [x for x in arr if x < pivot]
    middle = [x for x in arr if x == pivot]
    right = [x for x in arr if x > pivot]
    
    return quicksort(left) + middle + quicksort(right)

def randomized_quicksort(arr):
    if len(arr) <= 1:
        return arr
    
    pivot = random.choice(arr)
    left = [x for x in arr if x < pivot]
    middle = [x for x in arr if x == pivot]
    right = [x for x in arr if x > pivot]
    
    return randomized_quicksort(left) + middle + randomized_quicksort(right)

if __name__ == "__main__":
    # Generate random input data
    data_size = 10000
    data = [random.randint(1, 10000) for _ in range(data_size)]
    
    # Analyze deterministic Quick Sort
    start_time = time.time()
    sorted_data = quicksort(data)
    end_time = time.time()
    deterministic_time = end_time - start_time

    # Analyze randomized Quick Sort
    start_time = time.time()
    randomized_sorted_data = randomized_quicksort(data)
    end_time = time.time()
    randomized_time = end_time - start_time

    # Check if both sorting methods produce the same result
    assert sorted_data == randomized_sorted_data

    print(f"Data Size: {data_size}")
    print(f"Deterministic Quick Sort Time: {deterministic_time:.6f} seconds")
    print(f"Randomized Quick Sort Time: {randomized_time:.6f} seconds")
