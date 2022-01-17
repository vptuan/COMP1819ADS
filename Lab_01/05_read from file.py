#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Tue Jan 14 01:36:23 2020

@author: tuan
"""

f = open("lucky_ids.txt", "r")
for bannerId in f:
  print(bannerId, end="")