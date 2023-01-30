# -*- coding: utf-8 -*-
"""
Created on Tue Feb  2 10:41:28 2021

@author: Tuan Vuong
#
257, 3779, 14741, 331777, 7772777, 111181111, 99999199999 
"""

import time

n = 111181177 # 10 secs

start = time.time()

"""
The given code checks whether a given number n is a prime number or not. 
The is_prime variable is initialized as True. 
The code uses a for loop that iterates over a range of numbers from 2 to n-1. 
Inside the loop, the code checks if n is divisible by i (the current iteration number) by checking if n % i == 0. 
If it is divisible, it means i is a factor of n and n is not a prime number, so is_prime is set to False and the loop is broken. 
If the loop completes without finding a factor, is_prime remains True and n is considered a prime number.
"""
is_prime = True
for i in range(2, n):
    if n % i == 0:
        is_prime = False
        print("factor ", i)
        break
    else:
        is_prime = True

print(is_prime)

end = time.time()
print("n = {}; time = {}".format(n, end-start))
