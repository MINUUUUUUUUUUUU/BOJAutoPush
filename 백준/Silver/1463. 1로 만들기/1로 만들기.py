import sys

n = int(sys.stdin.readline())

dp = [n for _ in range(n+2)]
dp[0] = 0
dp[1] = 0
dp[2] = 1

if n < 3:
    print(dp[n])
    exit()

dp[3] = 1

if n == 3:
    print(dp[3])
    exit()

for i in range(1, n+1):
    if i / 6 == int(i/6):
        dp[i] = min(dp[i], dp[i//3] + 1, dp[i//2] + 1, dp[i-1] + 1)
    elif i / 3 == int(i/3):
        dp[i] = min(dp[i], dp[i//3] + 1, dp[i-1] + 1)
    elif i / 2 == int(i/2):
        dp[i] = min(dp[i], dp[i//2] + 1, dp[i-1] + 1)
    else:
        dp[i] = min(dp[i], dp[i-1] + 1)
        
print(dp[n])