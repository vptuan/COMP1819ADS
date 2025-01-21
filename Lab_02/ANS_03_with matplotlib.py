import time
import matplotlib.pyplot as plt

def detect_duplicate_nested(ids):
    """
    Detect the first duplicate ID in the list using nested loops.

    Parameters:
    - ids: List of integers.

    Returns:
    - The first duplicate value found, or None if no duplicate exists.
    """
    for i in range(len(ids)):
        for j in range(i + 1, len(ids)):
            if ids[i] == ids[j]:  # Check if a duplicate exists
                return ids[i]
    return None  # No duplicate found

# Measure running time for different input sizes
def measure_runtime_nested():
    input_sizes = [3, 100, 300, 600, 1000]
    runtimes = []

    for size in input_sizes:
        # Generate test data with a guaranteed duplicate
        ids = list(range(size)) + [size // 2]  # Add a duplicate in the middle

        # Measure runtime
        start_time = time.time()
        detect_duplicate_nested(ids)
        end_time = time.time()

        runtimes.append(end_time - start_time)

    # Plot the results
    plt.figure(figsize=(8, 6))
    plt.plot(input_sizes, runtimes, marker='o', label="Runtime (Nested Loops)")
    plt.title("Running Time of Duplicate Detection (Nested Loops)")
    plt.xlabel("Input Size (number of IDs)")
    plt.ylabel("Time (seconds)")
    plt.legend()
    plt.grid(True)
    plt.show()

    return runtimes

# Example Usage
ids = [1, 3, 4, 5, 3, 7, 8]
print(f"First duplicate found: {detect_duplicate_nested(ids)}")  # Output: 3

# Measure runtime and plot the graph
measure_runtime_nested()
