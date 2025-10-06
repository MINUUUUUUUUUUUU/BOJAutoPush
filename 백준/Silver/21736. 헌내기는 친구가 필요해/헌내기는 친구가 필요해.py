from collections import deque

n, m = map(int, input().split())

campus = list(list(map(str, input().strip())) for _ in range(n))
# print(campus)

visited = [[False for _ in range(m)] for _ in range(n)]

queue = deque()

for i in range(n):
    for j in range(m):
        if campus[i][j] == 'I':
            queue.append([i, j])
            break
            
# print(start)

answer = set()

dx = (1, -1, 0, 0)
dy = (0, 0, 1, -1)

# queue = deque([[start[0], start[1]]])

while queue:
# def dfs(x, y):
    
    x, y = queue.popleft()
    
    if campus[x][y] == 'P':
        answer.add((x, y))
    
    visited[x][y] = True
    
    for i in range(4):
        posx = x + dx[i]
        posy = y + dy[i]
        
        if posx >= 0 and posy >=0 and posx < n and posy < m and not visited[posx][posy] and (campus[posx][posy] != 'X'):
            # dfs(posx, posy)
            visited[posx][posy] = True
            queue.append([posx, posy])
            
# dfs(start[0], start[1])
t = len(answer)

if t == 0:
    print('TT')
else:
    print(t)