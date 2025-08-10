import sys
from collections import deque

t = int(sys.stdin.readline())

for _ in range(t):
    m, n, k = map(int, sys.stdin.readline().split())
    
    graph = [[0 for _ in range(n)] for _ in range(m)]
    bachus = set()
    
    for _ in range(k):
        tx, ty = map(int, sys.stdin.readline().split())
        graph[tx][ty] = 1
        bachus.add((tx,ty))
        
    cnt = 0
    visited = [[False for _ in range(n)] for _ in range(m)]
    dx = (1, -1, 0, 0)
    dy = (0, 0, 1, -1)
    
    def dfs(x, y):
        visited[x][y] = True
        
        for i in range(4):
            posx = x + dx[i]
            posy = y + dy[i]
            
            if posx >= 0 and posy >= 0 and posx < m and posy < n and not visited[posx][posy] and graph[posx][posy] == 1:
                dfs(posx, posy)
        
    for bachu in bachus:
        if not visited[bachu[0]][bachu[1]]:
            cnt += 1
            dfs(bachu[0], bachu[1])
    
    print(cnt)
        