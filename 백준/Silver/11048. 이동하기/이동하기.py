import sys

n, m = map(int, sys.stdin.readline().split())
maze = [list(map(int, sys.stdin.readline().split())) for _ in range(n)]
# direction = ((1, 0), (0, 1), (1, 1))

dp = [[0 for _ in range(m)] for _ in range(n)]
dp[0][0] = maze[0][0]

for i in range(n):
    for j in range(m):
        if i > 0:
            dp[i][j] = max(dp[i][j], dp[i-1][j] + maze[i][j])
        if j > 0:
            dp[i][j] = max(dp[i][j], dp[i][j-1] + maze[i][j])
        if i > 0 and j > 0:
            dp[i][j] = max(dp[i][j], dp[i-1][j-1] + maze[i][j])

print(dp[n-1][m-1])