"""
This video has NO Sound, so you can put on some MUSIC if you want

Spyder Editor: Spyder 4.2.1 

This demo is for Lab 01 - Ex1 MinMax function 
"""

def minmax(sequence):
    min = max = sequence[0] # assuming no-empty
    # PUT YOUR CODE HERE
    return (min,max)

# HOW TO TEST WITH DIFFERENT INPUTS
print(minmax([3])) # Test 3: correct
print(minmax([0,1,-2])) #Test 2: correct
print(minmax([1,2,3,5])) #Test 1: correct
print(minmax([10,0,-5,20,7,9,11])) # extra
# These are fixed values for inputs!