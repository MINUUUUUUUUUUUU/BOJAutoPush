n = int(input())

houses = []

for _ in range(n):
    houses.append(list(map(int, input().split())))
    
# print(houses)
dp = [[0, 0, 0] for _ in range(n)] # 해당 집에 RED, GREEN, BLUE로 칠해졌을 때의 최솟값

dp[0] = houses[0]
# print(dp)

for i in range(1, n):
    dp[i] = [min(dp[i-1][1], dp[i-1][2]) + houses[i][0], min(dp[i-1][0], dp[i-1][2]) + houses[i][1], min(dp[i-1][0], dp[i-1][1]) + houses[i][2]]
    
print(min(dp[-1]))