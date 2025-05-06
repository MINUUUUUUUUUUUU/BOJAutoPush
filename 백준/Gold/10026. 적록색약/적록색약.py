from collections import deque

n = int(input())

grid = []
for i in range(n):
    tmp = input()
    tmp_list = []
    for t in tmp:
        tmp_list.append(t)
    grid.append(tmp_list)

visited_n = [[False for i in range(n)] for j in range(n)] #normal
visited_cb = [[False for i in range(n)] for j in range(n)] #color blindness

direction = [[1,0] , [-1,0], [0,1], [0,-1]]

def bfs_n(graph, start, visited):
    queue = deque([start])
    visited[start[0]][start[1]] = True

    while queue:
        v = queue.popleft()
        # print(v, end = ' ')
        
        c = graph[v[0]][v[1]] # 현재 위치 색깔

        for d in direction:
            pos = [ v[0] + d[0] , v[1] + d[1] ]
            if pos[0] < 0 or pos[1] < 0 or pos[0] == n or pos[1] == n:
                continue
            
            if graph[pos[0]][pos[1]] != c:
                continue
            
            if not visited[pos[0]][pos[1]]:
                queue.append(pos)
                visited[pos[0]][pos[1]] = True

def bfs_cb(graph, start, visited):
    queue = deque([start])
    visited[start[0]][start[1]] = True

    while queue:
        v = queue.popleft()
        # print(v, end = ' ')
        
        c = graph[v[0]][v[1]] # 현재 위치 색깔깔
        
        if c is 'R' or c is 'G':
            c = 'RG'

        for d in direction:
            pos = [ v[0] + d[0] , v[1] + d[1] ]
            if pos[0] < 0 or pos[1] < 0 or pos[0] == n or pos[1] == n:
                continue
            
            if graph[pos[0]][pos[1]] is 'B':
                if c != 'B':
                    continue
            else:
                if c != 'RG':
                    continue
            
            if not visited[pos[0]][pos[1]]:
                queue.append(pos)
                visited[pos[0]][pos[1]] = True

count_n = 0
count_cb = 0

for i in range(n):
  for j in range(n):
    if not visited_n[i][j]:
        bfs_n(grid, [i, j], visited_n)
        count_n += 1
        
# print()

for i in range(n):
  for j in range(n):
    if not visited_cb[i][j]:
        bfs_cb(grid, [i, j], visited_cb)
        count_cb += 1
print(count_n, count_cb)