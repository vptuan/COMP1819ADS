student_one = '001143514'
student_two = '001062346'

def lucky_winner(id):
    f = open("lucky_ids.txt", 'r')
    for line in f.readlines():
        am_i_winner = False
        if line == id:
            am_i_winner = True
    if am_i_winner:
        return print("Yes")    
    print("No")

lucky_winner(student_one)
lucky_winner(student_two)
