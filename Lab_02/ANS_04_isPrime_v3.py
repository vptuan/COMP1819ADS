#n = int(input())

import time

n = 111181177 # 4 secs

start = time.time()

"""
The code checks whether a given number n is a prime number or not. 
If n is greater than 1, the code enters a for loop which runs from 2 to int(n/2). 
Within the loop, it checks if n is divisible by i using the modulo operator %. 
If the result is 0, it means that n is divisible by i and hence not prime, so is_prime is set to False and a message is printed with the factor i. 
If the result is not 0, it means that n is not divisible by i and the loop continues.
"""
is_prime = True

if n <= 1:
    is_prime = False
else:
    for i in range(2, int(n/2)):
        if n % i == 0:
            is_prime = False
            print("factor ", i)
            break

print(is_prime)

end = time.time()
print("n = {}; time = {}".format(n, end-start))
