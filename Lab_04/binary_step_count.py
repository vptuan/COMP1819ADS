# Binary step counts
n = 1_000_000
step = 0
while n>1:
    print(n)
    n = n // 2
    step+= 1

print(n)
print("Step", step)