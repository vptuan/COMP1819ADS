
# Function to do insertion sort
def insertion_sort(arr):

    # Traverse through 1 to len(arr)
    for i in range(1, len(arr)):
        key = arr[i]
        print ("Iter : ", i, arr)
		# Move elements of arr[0..i-1], that are
		# greater than key, to one position ahead
		# of their current position
        j = i-1
        while j >= 0 and key < arr[j] :
            arr[j + 1] = arr[j]
            print ("Moving : ", j, arr)
            j -= 1
        arr[j + 1] = key
        print ("Sett.. : ", j, arr)

arr = [6, 5, 3, 1, 8, 7, 2, 4]

print ("Insertion sort : ", arr)

insertion_sort(arr)

print("Output: ", arr)


 