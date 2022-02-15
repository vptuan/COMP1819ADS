def bubble_sort(arr):
    n = len(arr)

    # Traverse through all array elements
    swapFlag = False
    for i in range(n):
        print("Pass iter:", i)
        # Last i elements are already in place
        for j in range(0, n-i-1):

            # traverse the array from 0 to n-i-1
            # Swap if the element found is greater
            # than the next element

            if (arr[j] > arr[j+1]): # check for the wrong order
                    arr[j], arr[j+1] = arr[j+1], arr[j]
                    swapFlag = True
                    print ("Swap.. : ", arr[j+1], arr[j], arr)

        if (swapFlag == False):
            break
        
arr = [6, 5, 3, 1, 8, 7, 2, 4]

print ("Input : ", arr)

insertion_sort(arr)

print("Output: ", arr)