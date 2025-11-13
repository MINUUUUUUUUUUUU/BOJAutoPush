t = int(input())

dp = [[0, 0] for _ in range(41)] # [0의 개수, 1의 개수]
dp[0] = [1, 0]
dp[1] = [0, 1]

for i in range(2, 41):
    dp[i] = [dp[i-2][0] + dp[i-1][0], dp[i-2][1] + dp[i-1][1]]
    
# print(dp)

# def fibonacci(n):
#     if n == 0:
#         return 0;
#     elif n == 1:
#         return 1;
#     else:
#         return fibonacci(n-1) + fibonacci(n-2)

for _ in range(t):
    num = int(input())
    print(dp[num][0], dp[num][1])