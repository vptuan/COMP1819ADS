#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Tue Jan 14 01:35:38 2020

@author: tuan
"""

f = open("lucky_ids_4.txt", "r")
with open("lucky_ids_4.txt", "r") as f:
    ids = [int(x) for x in next(f).split()] # read first line
print(ids)
# YOUR CODE HERE
