# -*- coding: utf-8 -*-
"""
Created on Tue Feb  2 10:41:28 2021

@author: Tuan Vuong
"""

import time

n = 111181111

start = time.time()

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