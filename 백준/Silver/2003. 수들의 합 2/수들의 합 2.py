import sys

n, m = map(int, sys.stdin.readline().split())
A = list(map(int,sys.stdin.readline().split()))

answer = 0
start = 0
end = 1

while start < n and end < n+1:
    
    tmp = sum(A[start:end])
    if tmp == m:
        answer += 1
        start += 1
        end += 1
    elif tmp < m:
        end += 1
    elif tmp > m:
        start += 1

print(answer)