import sys

n, k = map(int, sys.stdin.readline().split())
cnt = 0 # 낙찰받은 갯수
# x = 100001
inc = []

for _ in range(n):
    a, b = map(int, sys.stdin.readline().split())
    
    if a >= b:
        cnt += 1
    else:
        inc.append(b-a)

inc.sort()

if cnt >= k:
    print("0")
else:
    print(inc[k-cnt-1])