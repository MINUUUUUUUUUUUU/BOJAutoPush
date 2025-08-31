import math

n = int(input())
m = int(input())

x = list(map(int, input().split()))

answer = x[0]

for i in range(m - 1):
    answer = max(answer, math.ceil((x[i+1] - x[i])/2) )
    
if n - x[-1] > answer:
    answer = n - x[-1]

print(answer)