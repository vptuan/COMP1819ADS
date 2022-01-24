# -*- coding: utf-8 -*-
"""
Created on Tue Jan 26 10:02:22 2021

@author: tuan
Using time function

"""
import time

def test_run():
    start = time.time()
    x = 1
    for i in range(0,100000000):
        x*=1.001
    end = time.time()
    print("The time taken is ", end-start, "seconds.")
    
if __name__ == "__main__":
    test_run()
