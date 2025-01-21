def find_two_numbers(numbers, target):
    """
    Find two numbers in the sorted array that add up to the target value.

    Parameters:
    - numbers: List of integers (sorted in non-decreasing order).
    - target: The target sum.

    Returns:
    - List containing the indices of the two numbers.
    """
    # Initialize two pointers
    left = 0
    right = len(numbers) - 1

    # Use the two-pointer technique
    while left < right:
        current_sum = numbers[left] + numbers[right]
        if current_sum == target:
            return [left, right]  # Return indices when the sum is found
        elif current_sum < target:
            left += 1  # Move the left pointer to increase the sum
        else:
            right -= 1  # Move the right pointer to decrease the sum

# Example Usage
numbers1 = [2, 7, 11, 15]
target1 = 9
print(find_two_numbers(numbers1, target1))  # Output: [0, 1]

numbers2 = [1, 2, 3, 4, 5]
target2 = 6
print(find_two_numbers(numbers2, target2))  # Output: [1, 3]
