def reverse_array(array):
    reversed_version = []
    while len(array):
        reversed_version.append(array[-1])
        array = array[:-1]
    return reversed_version

test = [1, 2 , 3, 4 ,5 ,6, 8, 121]
print(test)
test = reverse_array(test)
print(test)
