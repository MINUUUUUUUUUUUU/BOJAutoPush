import sys
from collections import deque

n = int(sys.stdin.readline())

maps = list(list(map(int, sys.stdin.readline().strip())) for _ in range(n))

# print(maps)

dx = (1, -1, 0, 0)
dy = (0, 0, 1, -1)

apartment = [[0 for _ in range(n)] for _ in range(n)]
cnt = [0 for _ in range(n * n)]

num = 0
for i in range(n):
    for j in range(n):
        if apartment[i][j] == 0 and maps[i][j] == 1:
            num += 1
            
            queue = deque([(i, j)])
            apartment[i][j] = num
            cnt[num] += 1
            
            while queue:
                x, y = queue.popleft()
                
                for k in range(4):
                    posx = x + dx[k]
                    posy = y + dy[k]
                    
                    if posx < 0 or posy < 0 or posx > n-1 or posy > n-1:
                        continue
                    
                    if maps[posx][posy] == 1 and apartment[posx][posy] == 0:
                        apartment[posx][posy] = num
                        cnt[num] += 1
                        queue.append((posx, posy))
                        
# for a in apartment:
#     print(a)

print(num)
answer = []

for c in cnt:
    if c != 0:
        answer.append(c)
        
answer.sort()
for i in range(0, num ):
    print(answer[i])