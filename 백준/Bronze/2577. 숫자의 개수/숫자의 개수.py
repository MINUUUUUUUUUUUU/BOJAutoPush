a = int(input())
b = int(input())
c = int(input())
m = a * b * c

l = [0 for i in range(10)]

s = str(m)
for i in s:
    l[int(i)] += 1

for i in l:
    print(i)