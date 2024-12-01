k = int(input())
stack = []

for i in range(k):
    tmp = int(input())
    if tmp == 0:
        stack.pop()
        continue
    stack.append(tmp)
    
print(sum(stack))