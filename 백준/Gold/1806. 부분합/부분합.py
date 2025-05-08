import sys

n, s = map(int, sys.stdin.readline().split())
seq = list(map(int,sys.stdin.readline().split()))

start = 0
end = 0

ans = 100001
tmp_sum = 0
l = 0

while start < n:
    
    if tmp_sum >= s:
        ans = min(ans, l)
        tmp_sum -= seq[start]
        start += 1
        l -= 1
    elif end == n:
        break
    else:
        tmp_sum += seq[end]
        end += 1
        l += 1
    
# print(cases)

if ans == 100001:
    print(0)
else:
    print(ans)