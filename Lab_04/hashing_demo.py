table = [None] * 11

def h(x):
    return x % 11

def insert(x):
    i = h(x)
    while table[i] is not None:
        i = (i + 1) % len(table)  # linear probing
    table[i] = x

values = [54, 26, 93, 17, 77, 31]
for v in values:
    insert(v)

print(table)
