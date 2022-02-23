def sumDigits(number): # n = 102
    return sum(int(digit) for digit in str(number))

def selection_sort(arr):
    for i in range(len(arr)):
        min_idx = i
        for j in range(i + 1, len(arr)):
            if sumDigits(arr[min_idx]) > sumDigits(arr[j]):
                min_idx = j
        arr[i], arr[min_idx] = arr[min_idx], arr[i]

arr = [12, 10, 102, 31, 15, 11]
print(arr)    
selection_sort(arr)
print(arr)