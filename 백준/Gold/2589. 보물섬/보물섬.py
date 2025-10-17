from collections import deque

n, m = map(int, input().split())

maps = list(list(map(str, input().strip())) for _ in range(n))

# L은 육지, W는 바다

dx = (1, -1, 0, 0)
dy = (0, 0, 1, -1)


def bfs(start, visited):
    queue = deque([start])
    visited[start[0]][start[1]] = 0
    
    while queue:
        v = queue.popleft() # v = [x,y] 형태
        k = visited[v[0]][v[1]]
        
        for i in range(4):
            posx = v[0] + dx[i]
            posy = v[1] + dy[i]
            
            if posx < 0 or posy < 0 or posx >= n or posy >= m:
                continue
            elif maps[posx][posy] == 'W':
                continue
            
            if visited[posx][posy] == -1:
                queue.append([posx, posy])
                visited[posx][posy] = k + 1
        
answer = 0

for i in range(n):
    for j in range(m):
        if maps[i][j] == 'W':
            continue
        
        visited = [[-1 for _ in range(m)] for _ in range(n)] #움직이는 시간을 기록
        bfs([i, j], visited)
        # print(visited)
        
        for visit in visited:
            answer = max(max(visit), answer)

print(answer)