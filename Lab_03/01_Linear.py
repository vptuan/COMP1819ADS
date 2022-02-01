# -*- coding: utf-8 -*-
"""
Created on Tue Feb  1 10:32:05 2022

@author: Tuan
"""
import time

def test_Linear(N):
    x = 0 
    for i in range(N):
        x+=i**1.001 # adding i^(1.001) to x
    return x

start = time.time()   
test_Linear(1000000)
end = time.time()
print("The time taken is ", end-start, "seconds.")