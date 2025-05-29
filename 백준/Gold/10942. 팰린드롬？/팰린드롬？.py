import sys

n = int(sys.stdin.readline())
numbers = list(map(int, sys.stdin.readline().split()))

dp = [[0 for _ in range(n)] for _ in range(n)]

## 1글자
for i in range(n):
    dp[i][i] = 1

## 2글자
for i in range(n-1):
    if numbers[i] == numbers[i+1]:
        dp[i][i+1] = 1

## 3글자 이상
for i in range(3, n + 1): # 3글자부터 글자 최대 길이까지
    for j in range(0, n - i + 1):
        k = j + i - 1 # 끝 지점 (시작점은 j)
        if numbers[k] == numbers[j] and dp[j+1][k-1] == 1:
            dp[j][k] = 1

# print(dp)        

m = int(sys.stdin.readline())
for _ in range(m):
    s, e = map(int, sys.stdin.readline().split())
    print(dp[s-1][e-1])