s = input()

numbers = s.split('-')
result = 0
first = 0

for i in numbers:
    tmp = []
    tmp = i.split('+')
    if first == 0:
        for j in tmp:
            result += int(j)
        first = 1
    else:
        for j in tmp:
            result -= int(j)

print(result)