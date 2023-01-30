import math
import time

def isPrime(n): # not correct for n == 2
    if n == 2: return True
    if (n % 2 == 0):
        return False
    for i in range(3, int(math.sqrt(n)) + 1, 2): # all odds, between 3, sqrt(n)
        if n % i == 0:
            print("factor ", i)
            return False
    return True


#r = (7772777, 111181111, 99999199999,67280421310721,311111111111113,9999999900000001)
r = [3,111181177] # 0 sec
for i in r:
    start = time.time()
    print(isPrime(i))
    end = time.time()
    print("n = {}; time = {}".format(i, end-start))
