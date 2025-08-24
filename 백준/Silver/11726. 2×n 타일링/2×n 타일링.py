import sys

num = int(sys.stdin.readline())

mm = [0 for _ in range(num + 1)]


def dp(n):
    if n == 1 or n == 2 or n == 3:
        return n
    elif mm[n] != 0:
        return mm[n]
    else:
        mm[n] = dp(n-1) + dp(n-2)
        return mm[n]
        
print(dp(num) % 10007)