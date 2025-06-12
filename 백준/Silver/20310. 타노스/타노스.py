import sys
num = list(map(int, sys.stdin.readline().strip()))
l = len(num)

ones = sum(num)
zeros = l - ones

# print(ones, zeros)

tanos_ones = ones // 2
tanos_zeros = zeros // 2

i = 0
idx = set()
while i < l:
    if num[i] == 1 and tanos_ones > 0:
        idx.add(i)
        tanos_ones -= 1
    if num[-(i+1)] == 0 and tanos_zeros > 0:
        idx.add(l-(i+1))
        tanos_zeros -= 1
    
    i += 1

# print(idx)
answer = []

for i in range(l):
    if i in idx:
        continue
    else:
        answer.append(str(num[i]))
print(''.join(answer))