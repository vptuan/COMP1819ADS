"""
This solution is for Lab 01 - Ex1 MinMax function with user's inputs 
"""
def min_max(number_list):
    if len(number_list) == 0:
        return ()

    min_number = number_list[0]
    max_number = number_list[0]

    for number in number_list:
        if number > max_number:
            max_number = number
        if number < min_number:
            min_number = number
    
    return (min_number, max_number)

print("Insert a list of numbers. In this format: \"1, 2.0, 5.5\"")
user_input = input("List of Numbers: ")
user_input = user_input.replace(" ", "")
number_list = user_input.split(",")

for i in range(0, len(number_list)): 
    number_list[i] = float(number_list[i])

print(min_max(number_list))