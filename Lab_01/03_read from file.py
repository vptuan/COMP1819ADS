#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Mon Jan 13 18:10:14 2020

@author: tuan
"""

f = open("lucky_ids.txt", "r")
for bannerId in f:
  print(bannerId, end="")