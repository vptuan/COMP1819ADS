# -*- coding: utf-8 -*-
"""
Created on Thu Jan  6 16:48:04 2022

@author: Tuan

"""
#!/bin/python3

if __name__ == '__main__':
    n = int(input().strip())
    if (n % 2 == 1): 
        print("Weird")
    else :
        if (2<= n <= 9):
            print("Not Weird")
        elif (10<= n <= 30):
            print("Weird")
        elif (30 < n):
            print("Not Weird")
