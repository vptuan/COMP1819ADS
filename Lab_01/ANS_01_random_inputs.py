#!/usr/bin/env python3
"""
This solution is for Lab 01 - Ex1 MinMax function with random inputs 
"""
def fMinMax(xSeqIn):
  tSeqList = tuple(xSeqIn)
  if len(tSeqList)<1:
    raise Exception
# short solution using min()/max()
# return tuple((min(tSeqList), max(tSeqList)))
  nMin = None
  nMax = None
  for nValue in tSeqList:
    if type(nValue) == int or type(vValue) == float:
      if nMin == None:
        nMin = nValue
        nMax = nValue
      else:
        if nValue >nMax:
          nMax = nValue
        elif nValue<nMin:
          nMin = nValue
    else:
      raise Exception
  return (nMin, nMax)



if __name__ == '__main__':

  import random
  t = []
  for k in range(int(random.random()*7+3)):
    t.append(int(random.random()*20-10))
  print(t)
  print(fMinMax(t))
