s = input()

zeroset = 0
oneset = 0
status = -1

for i in s:
    if i == '0':
        if status != 0:
            status = 0
            zeroset += 1
    elif i == '1':
        if status != 1:
            status = 1
            oneset += 1
            
# print(zeroset, oneset)
print(min(zeroset, oneset))