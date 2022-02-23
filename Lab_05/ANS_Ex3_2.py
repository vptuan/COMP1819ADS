list1 = [12, 10, 102, 31, 15]
list2 = [14, 1101, 10, 35, 0]

def sortBySum(lst):
    sumDict = {}
    for i in lst:
        sumDict[i] = 0
        for digit in str(i):
            sumDict[i] += int(digit)
    
    #Bubble sort.
    for i in range(len(lst)):
        swapFlag = False
        for j in range(0, len(lst)-i-1):
            if (sumDict[lst[j]] > sumDict[lst[j+1]]):
                lst[j], lst[j+1] = lst[j+1], lst[j]
                swapFlag = True
        if (swapFlag == False):
            break

print("Unsorted:")
print(list1)
print(list2)

sortBySum(list1) #[10, 12, 102, 31, 15]
sortBySum(list2) #[0, 10, 1101, 14, 35]

print("Sorted:")
print(list1)
print(list2)
