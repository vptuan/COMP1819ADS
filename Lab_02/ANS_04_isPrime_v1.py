# -*- coding: utf-8 -*-
"""
Created on Tue Feb  2 10:43:31 2021

@author: Tuan Vuong
#
257, 3779, 14741, 331777, 7772777, 111181111, 99999199999 

"""

import time

n = 111181177 # 8 secs

start = time.time()

# factors is a list of integers from 1 to n (inclusive), such that n is divisible by f.
# The expression f for f in range(1, n+1) creates a sequence of numbers from 1 to n (inclusive) and assigns each number to the variable f. 
# The if clause if n % f == 0 specifies that only the elements of the sequence for which the condition n % f == 0 is true should be included in the resulting list. 
# The % operator represents modulo, so n % f == 0 is true if and only if n is divisible by f.
factors = [f for f in range (1,n+1) if n%f==0 ]

print(factors)

# is_prime when a numbers having exactly 2 factors
is_prime = len(factors) == 2

print(is_prime)

end = time.time()
print("n = {}; time = {}".format(n, end-start))
