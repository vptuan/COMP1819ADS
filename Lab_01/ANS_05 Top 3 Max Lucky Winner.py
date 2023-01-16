# Can you spot a bug
with open("lucky_ids_4.txt", "r") as f:
    stuff = []
    for i in f.readline().split():
        stuff.append(int(i))
    greatest1 = stuff[0]
    greatest2 = stuff[0]
    greatest3 = stuff[0]
    for i in stuff:
        if i > greatest1:
            greatest3 = greatest2
            greatest2 = greatest1
            greatest1 = i
        elif greatest1 > i > greatest2:
            greatest3 = greatest2
            greatest2 = i
        elif greatest2 > i > greatest3:
            greatest3 = i
        # print(i, greatest1, greatest2, greatest3)
    print(greatest1, greatest2, greatest3)
