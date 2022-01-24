"""
This video has NO SOUND

Spyder Editor: Spyder 4.2.1 

This demo is for Lab 02 - Ex Top 3 Max function 
"""
import time

def findmax(sequence): #find max and the index of max
    max = sequence[0] # assuming no-empty
    index = 0

    # YOUR CODE HERE
    
    return (max,index)

start = time.time()

# These are fixed values for inputs!
input = [10,0,-5,20,7,9,11]

# TOP1
print(input)
max1, index = findmax(input)
print(max1, index) 
input.remove(max1) # Remove max (TOP1) from the input

#TOP2
print(input)
max2, index = findmax(input)
print(max2, index) 
input.remove(max2) # Remove max(TOP2) from the input

#TOP3
print(input)
max3, index = findmax(input)
print(max3, index) # Remove max(TOP3) from the input

print(max1, max2, max3)

print("The time taken is ", time.time()-start, "seconds.")
# Is this always correct?
# Can you improve this further?