import sys
from collections import deque

n, m = map(int, sys.stdin.readline().split())
ground = list( list(map(int, sys.stdin.readline().split())) for _ in range(n) )


distance = [[-1 for _ in range(m)] for _ in range(n)]

for i in range(n):
    for j in range(m):
        if ground[i][j] == 2:
            dest_x = i
            dest_y = j
        elif ground[i][j] == 0:
            distance[i][j] = 0

# print(dest_x, dest_y)
# print(distance)

dx = (0, 0, 1, -1)
dy = (1, -1, 0, 0)

queue = deque([(dest_x, dest_y, 0)]) # X, Y, cnt
distance[dest_x][dest_y] = 0

while queue:
    x, y, c = queue.popleft()
    # print("X", x, "Y", y, "C", c)
    
    for i in range(4):
        posx = x + dx[i]
        posy = y + dy[i]
        
        if posx < 0 or posy < 0 or posx > n-1 or posy > m-1:
            continue
        
        if ground[posx][posy] == 1 and distance[posx][posy] == -1:
            distance[posx][posy] = c+1
            queue.append((posx, posy, c+1))

for i in range(n):
    for j in range(m):
        if j == m-1:
            print(distance[i][j])
        else:
            print(distance[i][j], end=' ')
    