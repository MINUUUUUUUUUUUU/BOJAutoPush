import sys

t = int(sys.stdin.readline())


k = 15
n = 14

dp = [[i for i in range(1, n + 1)] for _ in range(k)]

for i in range(1, k):
    for ii in range(n):
        tmp = 0
        for iii in range(ii+1):
            tmp += dp[i-1][iii]
        dp[i][ii] = tmp

# for d in dp:
#     print(d)

for _ in range(t):
    a = int(sys.stdin.readline())
    b = int(sys.stdin.readline())
    
    print(dp[a][b-1])