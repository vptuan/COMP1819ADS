import time

def constant(n):
    x = 0
    count = 0
    for x in range(10000):
        x = x + len(n)
        count += 1
    return count

def linear(n):
    x = 0
    count = 0
    for i in n:
        x = x + i
        count += 1
    return count

def quadratic(n):
    count = 0
    for i in n:
        for j in n:
            x += i * j
            count += 1
    return count

def timetaken(size):
    sequence = []
    for i in range(size):
        sequence.append(i)
    starttime = time.time()
    ######################## select Big-0 here ########################
    constant(sequence)
    #linear(sequence)
    #quadratic(sequence)
    ######################## select Big-0 here ########################
    totaltime = time.time() - starttime
    return (totaltime)


def runCases(caseSizes):
    print("Size  Timetaken(Standard Form)  Timetaken (Decimal)")
    for n in caseSizes:
        tk = timetaken(n)
        print(str(n)+"  "+ str(tk)+ " " + format(tk, ".2f"))

#numbersizes = [1024,1000,10000,100000,10000000,20000000,100000000,200000000]
caseSizes = [10000,10000,10000]

runCases(caseSizes)
