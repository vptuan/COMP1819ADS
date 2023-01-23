import time

'''
The time complexity of the following code is O(1) (constant time). 
The loop iterates a fixed number of times (10000), regardless of the value of the input variable n. 
The operations performed inside the loop also have a constant time complexity. 
The time taken to execute this code will always be the same and does not depend on the size of the input variable n.
'''
def constant(n):
    x = 0
    count = 0
    for x in range(10000):
        x = x + len(n)
        count += 1
    return count

'''
The time complexity of the function 'linear(n)' is O(n) 
because the number of operations being performed is directly proportional to the size of input n. 
The function is iterating through the input list 'n' and 
performing an operation on each element, so the number of operations is directly proportional to the number of elements in the list.
'''
def linear(n):
    x = 0
    count = 0
    for i in n:
        x = x + i
        count += 1
    return count

'''
The time complexity of the following code is O(n^2), also known as quadratic. 
The inner loop iterates through the entire input size "n" for each iteration of the outer loop, 
thus resulting in a total of n*n operations, or n^2 operations.
'''
def quadratic(n):
    count = 0
    for i in n:
        for j in n:
            x += i * j
            count += 1
    return count

'''
The runCase function creates a sequence of integers of the given size, gets the current time 
and calls the function whose time complexity is being analyzed (constant, linear, or quadratic). 
The function then calculates the total time taken by subtracting the current time from the start time. 
'''
def runCase(size):
    #creates a list sequence of integers from 0 to size-1 using a for loop
    sequence = []
    for i in range(size):
        sequence.append(i)
        
    #starts a timer
    starttime = time.time()
    
    #calls one of the functions constant(sequence), linear(sequence), or quadratic(sequence), depending on which one is enabled. 
    constant(sequence)
    #linear(sequence)
    #quadratic(sequence)
    
    #calculates the total time taken by subtracting the start time from the current time. 
    totaltime = time.time() - starttime
    
    return (totaltime)

'''
The function runCases takes in a list of case sizes.
For each size in the list, it calls the runCase function passing the size as an argument. 
The function then prints out the size, the time taken in standard form, and the time taken in decimal form. 
The function runCases is used to report the time complexity of the different functions (constant, linear, or quadratic) with different sizes.
'''
def runCases(caseSizes):
    print("Size  Timetaken(Standard Form)  Timetaken (Decimal)")
    for n in caseSizes:
        tk = runCase(n)
        print(str(n)+"  "+ str(tk)+ " " + format(tk, ".2f"))

caseSizes = [10000,10000,10000]

runCases(caseSizes)
