import sys

n = int(sys.stdin.readline())
maze = list(map(int, input().split()))
dp = [n for _ in range(n)]
dp[0] = 0

for i in range(n):
    jump = maze[i]
    
    for k in range(1, jump+1):
        if i + k < n:
            dp[i + k] = min(dp[i + k], dp[i] + 1)

tmp = dp[n-1]
if tmp == n:
    print(-1)
else:
    print(tmp)