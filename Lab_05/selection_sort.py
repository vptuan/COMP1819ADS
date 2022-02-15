# Traverse through all array elements 


def selection_sort(arr):
    for i in range(len(arr)):

        # Find the minimum element in remaining
        # unsorted array
        print ("Iter :", i, arr)
        min_idx = i
        for j in range(i + 1, len(arr)):
            if arr[min_idx] > arr[j]:
                min_idx = j

            # Swap the found minimum element with
        # the first element
        arr[i], arr[min_idx] = arr[min_idx], arr[i]

arr = [6, 15, 3, 21, 38, 7, 2, 4]

print ("Input : ", arr)

selection_sort(arr)

print("Output: ", arr)