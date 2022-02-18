# Sample solution from a student in COMP1819-2022
import time

def constant(n):
    x = 0
    for x in range(10000):
        x = x + len(n)



def logarithmic(n):
    x = len(n)
    count = 0
    while x >1:
        x = x / 2
        count = count + 1



def linear(n):
    x = 0
    for i in n:
        x = x + i


def linear_logarithmic(n):
    x = len(n)
    count = 0
    for y in range(len(n)):
        x = len(n)
        while x > 1:
            x = x / 2
            count = count + 1


def square(n):
    for i in n:
        n[i] = i * 2
        for x in n:
            n[i] = i * 2


def cube(n):
    for i in n:
        n[i] = i * 2
        for x in n:
            n[i] = i * 2
            for y in n:
                n[i] = i * 2


def timetaken(size):
    sequence = []
    for i in range(size):
        sequence.append(i)
    starttime = time.time()
    ######################## select Big-0 here ########################
    #constant(sequence)
    #logarithmic(sequence)
    #linear(sequence)
    #linear_logarithmic(sequence)
    #square(sequence)
    #cube(sequence)
    ######################## select Big-0 here ########################
    totaltime = time.time() - starttime
    return (totaltime)


def graphing(testnumbers):
    print("__________GRAPHING__________")
    for i in testnumbers:
        print(str(i)+"  "+str(timetaken(i)))

numbersizes = [1024,1000,10000,100000,10000000,20000000,100000000,200000000]
graphing(numbersizes)
