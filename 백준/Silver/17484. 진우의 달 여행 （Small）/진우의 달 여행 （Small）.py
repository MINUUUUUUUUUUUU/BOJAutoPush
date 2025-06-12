import sys

n, m = map(int, sys.stdin.readline().split())

space = list(list(map(int, sys.stdin.readline().split())) for _ in range(n))

# dx = [1, 1, 1] # 코드의 가독성을 위해 일시 작성
dy = [-1, 0, 1]

# visited = [[False for _ in range(m)] for _ in range(n)]

result = 0
cases = set()

def dp(flag, posx, posy, cost):
    if posx == n-1:
        cases.add(cost)
        return
    
    posx += 1
    
    if flag != 1:
        # 1번 움직임
        if posy != 0:
            posy -= 1
            cost += space[posx][posy]
            dp(1, posx, posy, cost)
            cost -= space[posx][posy]
            posy += 1
    
    # 2번 움직임
    if flag != 2:
        cost += space[posx][posy]
        dp(2, posx, posy, cost)
        cost -= space[posx][posy]
    
    if flag != 3:
        # 3번 움직임
        if posy != m-1:
            posy += 1
            cost += space[posx][posy]
            dp(3, posx, posy, cost)
            cost -= space[posx][posy]
            posy -= 1
        
for i in range(m):
    # posx = 0
    posy = i
    
    dp(0, 0, i, space[0][i])
    
print(min(cases))