from collections import deque

n, m = map(int, input().split())
d = [[] for i in range(n)]

for i in range(n):
    tmp = input()
    for j in tmp:
        d[i].append(int(j))

# 상하좌우 순
dx = [-1, 1, 0, 0]
dy = [0, 0, 1, -1]

def bfs(d, n, m):
    queue = deque([(0,0)])
    
    while queue:
        x, y = queue.popleft()
        for i in range(4):
            nx = x + dx[i]
            ny = y + dy[i]
            
            if nx < 0 or nx >= n or ny < 0 or ny >= m:
                continue
            
            if d[nx][ny] == 0:
                continue
            
            if d[nx][ny] == 1:
                d[nx][ny] = d[x][y] + 1
                queue.append((nx,ny))
    return d[n-1][m-1]
    
print(bfs(d,n,m))