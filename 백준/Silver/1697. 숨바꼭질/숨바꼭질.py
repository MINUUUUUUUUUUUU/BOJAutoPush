import sys
from collections import deque

n, k = map(int, sys.stdin.readline().split())
visited = [False for _ in range(100001)]

queue = deque([(n, 0)]) # 수빈이의 위치, 걸리는 시간
visited[n] = True

while queue:
    v = queue.popleft()
    # print(v, end= ' ')
    
    if v[0] == k:
        print(v[1])
        exit()
    
    pos1 = v[0] + 1
    pos2 = v[0] - 1
    pos3 = 2 * v[0]
    
    if pos1 < 100001 and not visited[pos1]:
        queue.append((pos1, v[1] + 1))
        visited[pos1] = True
    if pos2 > -1 and not visited[pos2]:
        queue.append((pos2, v[1] + 1))
        visited[pos2] = True
    if pos3 < 100001 and not visited[pos3]:
        queue.append((pos3, v[1] + 1))
        visited[pos3] = True