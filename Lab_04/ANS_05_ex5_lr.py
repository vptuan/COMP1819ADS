arr = [6, 5, 3, 1, 8, 7, 2, 4]

l = 0
r = len(arr)-1
while (l<r):
    arr[l], arr[r] = arr[r], arr[l]
    l+= 1; r-=1 
    
print(arr) 
    