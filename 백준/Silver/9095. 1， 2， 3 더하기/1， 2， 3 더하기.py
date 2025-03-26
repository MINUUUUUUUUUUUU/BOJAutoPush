def calculate_123 (n):
    if n==1:
        return 1
    elif n==2:
        return 2
    elif n==3:
        return 4
    else:
        return calculate_123(n-1) + calculate_123(n-2) + calculate_123(n-3)

t = int(input()) ## 테스트 개수
answer = []

for i in range(t):
    print(calculate_123(int(input())))
    
    
