def gcd(a,b):
    if a % b == 0:
        return b
    else:
        return gcd(b, a%b)


n,m = map(int,input().split())
k = gcd(n,m)
for i in range(k):
    print(1, end='')