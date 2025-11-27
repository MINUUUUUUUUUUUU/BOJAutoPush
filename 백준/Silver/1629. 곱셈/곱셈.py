A, B, C = map(int, input().split())

# a ** b % c

# (a * a * a * a * a * ... * a) - c * ? = 답

def iwannabetheboshy(a, b, c):
    if b == 0:
        return 1
    if b % 2 == 0:
        half = iwannabetheboshy(a, int(b / 2), c)
        return (half * half) % c
    elif b % 2 == 1:
        return (iwannabetheboshy(a, b - 1, c) * a) % c
    
print(iwannabetheboshy(A, B, C))