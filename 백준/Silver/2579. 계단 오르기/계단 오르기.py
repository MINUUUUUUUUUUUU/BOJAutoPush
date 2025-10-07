n = int(input())

stairs = [int(input()) for _ in range(n)]
# print(stairs)

if n == 1:
    print(stairs[0])
    exit()
elif n == 2:
    print(stairs[0] + stairs[1])
    exit()

dp = [[0, 0] for _ in range(n)]

dp[0][0] = stairs[0] # 첫번째 계단 한번에
dp[1][0] = stairs[1] # 두번째 계단 한번에

dp[1][1] = stairs[0] + stairs[1] # 두번째 계단 두번에

for i in range(2, n):
    dp[i][0] = max(dp[i][0], dp[i-2][0] + stairs[i], dp[i-2][1] + stairs[i])
    dp[i][1] = max(dp[i][1] + stairs[i], dp[i-1][0] + stairs[i])
    
print(max(dp[i][0], dp[i][1]))