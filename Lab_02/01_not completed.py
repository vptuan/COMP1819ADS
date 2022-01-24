"""
This video has NO Sound

Spyder Editor: Spyder 4.2.1 

This demo is for Lab 02 - Ex1 MinMax function 
"""
import time

def minmax(sequence):
    min = max = sequence[0] # assuming no-empty
    for val in sequence:
        if (val > max):
            max = val
        if (val < min):
            min = val
    return (min,max)

#print(minmax([1,2,3,5])) 

def measure_time(input_size):
    sequence = [i for i in range(input_size)] # input = a list [0,1,2,...]
    print(sequence)
    start = time.time() # start timer
    print(minmax(sequence)) # execute the method minmax
    print("Input size=", input_size, " Time taken=", time.time()-start)


k = 10
measure_time(k)

# Now, we make input size larger, 2k, 10k,50k, 200k,1000k 
# YOUR CODE HERE