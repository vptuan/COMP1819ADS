def bubble_sort(arr, asc=True):
    n = len(arr)

    # Traverse through all array elements

    for i in range(n):
        swapFlag = False
        # Last i elements are already in place
        print ("Pass iter : ", i)
        for j in range(0, n-i-1):
            # traverse the array from 0 to n-i-1
            # Swap if the element found is greater
            # than the next element

            if (asc and arr[j] > arr[j+1]) or (not asc and arr[j] < arr[j+1]):
                    arr[j], arr[j+1] = arr[j+1], arr[j]
                    swapFlag = True
                    print ("Swap.. : ", arr[j+1], arr[j], arr)
        if (swapFlag == False):
            break

arr = [6, 5, 3, 1, 8, 7, 2, 4]
arr = [7,8,1]

print ("Input : ", arr)

bubble_sort(arr, True)

print("Output: ", arr)