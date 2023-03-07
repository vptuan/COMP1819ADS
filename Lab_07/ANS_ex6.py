#https://towardsdatascience.com/master-python-dictionary-for-beginners-in-2021-1cdbaa17ec45

# dictionary and set()
# dictionary: key-value pair 
# set: store unique values

def uniqueOccurrences(arr):
    
    dictionary = {}             
        
    for i in arr: 
        if i in dictionary: 
            dictionary[i]+=1
                
        else:
            dictionary[i]=1
                
    return len(dictionary.values()) == len(set(dictionary.values()))

# test case 
arr = [1,2,2,1,1,3]
uniqueOccurrences(arr)