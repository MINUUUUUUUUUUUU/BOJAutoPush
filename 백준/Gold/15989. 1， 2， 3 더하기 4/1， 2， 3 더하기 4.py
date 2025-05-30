import sys

t = int(sys.stdin.readline())
dp = [1 for _ in range(10001)]

for i in range(2, 10001):
    dp[i] += dp[i-2]
for j in range(3, 10001):
    dp[j] += dp[j-3]
    
for _ in range(t):
    n = int(sys.stdin.readline())
    print(dp[n])