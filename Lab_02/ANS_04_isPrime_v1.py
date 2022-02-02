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

factors = [f for f in range (1,n+1) if n%f==0 ]
print(factors)

is_prime = len(factors) == 2

print(is_prime)

end = time.time()
print("n = {}; time = {}".format(n, end-start))