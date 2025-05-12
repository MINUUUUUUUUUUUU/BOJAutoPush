import sys
from collections import deque

n, m = map(int, sys.stdin.readline().split())
board = [list(map(int, sys.stdin.readline().strip())) for _ in range(n)]

direction = [ (-1,0),(1,0),(0,1),(0,-1) ]

visited = [[[False, False] for _ in range(m)] for _ in range(n)] #0은 안부순상태, 1은 부순상태

queue = deque([(0, 0, 1, 0)]) # X좌표, Y좌표, 움직인 횟수, 벽부수기(0 == 이용안함)
visited[0][0][0] = True

while queue:
    v = queue.popleft()
    # print(v, end='')
    
    if v[0] == n-1 and v[1] == m-1:
            print(v[2])
            exit()
    
    for d in direction:
        pos = ( v[0] + d[0] , v[1] + d[1], v[2] + 1, v[3] )
        if pos[0] < 0 or pos[1] < 0 or pos[0] > n-1 or pos[1] > m-1:
            continue
        
        tmp_pos = board[ pos[0] ][ pos[1] ]
        
        if tmp_pos == 1 and pos[3] == 0 and not visited[pos[0]][pos[1]][1]:
            queue.append( ( pos[0], pos[1], pos[2], 1 ) )
            visited[pos[0]][pos[1]][1] = True
            
        if not visited[pos[0]][pos[1]][pos[3]] and tmp_pos == 0:
            queue.append(pos)
            visited[pos[0]][pos[1]][pos[3]] = True
            
print(-1)
        