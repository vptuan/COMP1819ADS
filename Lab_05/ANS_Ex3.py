def sumDigits(n): # n = 102
    s = 0 
    while n > 0:
        s = s+ n % 10 # add the last digit of n to s
        n = n // 10 # remove the last digit
    return s

def bubble_sort(arr):
    n = len(arr)

    swapFlag = False
    for i in range(n):

        # Last i elements are already in place
        for j in range(0, n-i-1):

            # traverse the array from 0 to n-i-1
            # Swap if the element found is greater
            # than the next element

            if (sumDigits(arr[j]) > sumDigits(arr[j+1])): # check for the wrong order
                    arr[j], arr[j+1] = arr[j+1], arr[j]
                    swapFlag = True

        if (swapFlag == False):
            break

arr = [12, 10, 102, 31, 15]
print(arr)    
bubble_sort(arr)
print(arr)