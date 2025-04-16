from itertools import permutations

n = int(input())
numbers = list(map(int,input().split()))
sign_count = list(map(int,input().split()))
sign = []

for i in range(sign_count[0]):
    sign.append('+')
for i in range(sign_count[1]):
    sign.append('-')
for i in range(sign_count[2]):
    sign.append('*')
for i in range(sign_count[3]):
    sign.append('/')

cases = set(permutations(sign, n-1))
# print(cases)
max = -1000000001
min = 1000000001

for case in cases:
    
    idx = 1 ## numbers[0] 값은 바로 대입
    result = numbers[0]
    
    for c in case:
        if c is '+':
            result += numbers[idx]
            idx += 1
        elif c is '-':
            result -= numbers[idx]
            idx += 1
        elif c is '*':
            result *= numbers[idx]
            idx += 1
        elif c is '/':
            result = int(result / numbers[idx])
            idx += 1
            
    if result > max:
        max = result
    
    if result < min:
        min = result
        
print(max)
print(min)