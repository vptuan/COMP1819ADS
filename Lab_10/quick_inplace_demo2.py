# -*- coding: utf-8 -*-
"""
Created on Fri Mar 26 14:45:03 2021

@author: tv6249tw
"""
def inplace_quick_sort(S, a, b, level):
  """Sort the list from S[a] to S[b] inclusive using the quick-sort algorithm."""
  if a >= b: return                                      # range is trivially sorted
  
  print("   "*level,"Level: ", level)
  print("   "*level,"Sorting: ", a, b, S[a:b+1])
  pivot = S[b]                                           # last element of range is pivot
  print("   "*level,"Pivot =", pivot)
  left = a                                               # will scan rightward
  right = b-1                                            # will scan leftward
  while left <= right:
    # scan until reaching value equal or larger than pivot (or right marker)
    while left <= right and S[left] < pivot:
      left += 1
    # scan until reaching value equal or smaller than pivot (or left marker)
    while left <= right and pivot < S[right]:
      right -= 1
    if left <= right:                                    # scans did not strictly cross
      S[left], S[right] = S[right], S[left]              # swap values
      print("   "*level,"Swapped ", S[right], S[left], S)
      left, right = left + 1, right - 1                  # shrink range

  # put pivot into its final place (currently marked by left index)
  print("   "*level,"Final left index", left) 
  S[left], S[b] = S[b], S[left]
  print("   "*level,"Final swap ", S[a:b+1])
  # make recursive calls
  inplace_quick_sort(S, a, left - 1, level+1)
  inplace_quick_sort(S, left + 1, b, level+1)
  
S = [85, 24, 63, 45, 17, 31, 96, 50]

inplace_quick_sort(S, 0, len(S)-1, 0)

print(S)