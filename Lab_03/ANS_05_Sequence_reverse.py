import time

stack = __import__('ANS_3_ArrayStack') #ArrayStack file
my_stack = stack.ArrayStack()


def populate_stack():
    my_stack.push(5)
    my_stack.push(3)
    print(my_stack.pop())
    print(my_stack.is_empty())
    print(my_stack.pop())
    my_stack.push(7)
    my_stack.push(9)
    my_stack.push(4)
    print(my_stack.pop())
    my_stack.push(6)
    my_stack.push(8)
    print(my_stack._data)


populate_stack()


def reverse(_stack):
    items = []
    while not _stack.is_empty():
        items.append(_stack.pop())
    print(items)
    for item in items:
        _stack.push(item)


start = time.time()
reverse(my_stack)
end = time.time()
print(my_stack._data)
print(f'The total time take is {end-start} seconds')
