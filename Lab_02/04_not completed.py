"""
Created on Mon Jan 24 20:08:49 2022

@author: tuan
"""

import sys
import time
def is_prime_number(num):
    """
    What is the time complexity of this method once its done?
    """
    if num == 0 or num == 1:
        return False
    
    # YOUR CODE HERE
    
    return True


if __name__ == "__main__":
    num = 3
    if len(sys.argv) < 2:
        num = int(input("Please insert a number: "))
        #r = (7772777, 111181111, 99999199999,67280421310721,311111111111113,9999999900000001)
    else:
        num = int(sys.argv[1])        
    t1 = time.time()
    print(is_prime_number(num))
    
    t2 = time.time()
    print("The algorithm took", str(t2 - t1), "seconds to complete.")

    