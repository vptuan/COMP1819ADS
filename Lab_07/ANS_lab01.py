# -*- coding: utf-8 -*-
"""
Created on Tue Mar  2 15:39:56 2021

@author: Ivo & Tuan
"""
from itertools import islice, chain
from random import choice
import time
from unsorted_table_map import UnsortedTableMap

random_str = "Test"
empty_dict = dict()
full_dict = dict()
for i in range(10000000):
    full_dict[i] = random_str

# Insert 10 000 new values into a full dictionary:
start = time.time()
for i in range(10000001, 10010002):
    full_dict[i] = random_str
print("Full dictionary", time.time() - start)  # 0.0019936561584472656
# Insert 10 000 new values into an empty dictionary:
start = time.time()
for i in range(10000001, 10010002):
    empty_dict[i] = random_str
print("Empty dictionary", time.time() - start)

# Insert 10 000 new values into a UnsortedTableMap:
dict = UnsortedTableMap()
start_time = time.time()
for i in range(10000001, 10010002):
    dict[i] = random_str
# print(dict[10000001])

print("\nUnsortedTableMap: ", time.time() - start_time)