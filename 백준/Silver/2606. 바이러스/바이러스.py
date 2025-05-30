import sys
from collections import deque

n = int(sys.stdin.readline())
m = int(sys.stdin.readline())
graph = [[] for _ in range(n)]

for _ in range(m):
    a, b = map(int, sys.stdin.readline().split())
    graph[a-1].append(b-1)
    graph[b-1].append(a-1)
    
queue = deque([0])
visited = [False for _ in range(n)]
visited[0] = True

while queue:
    v = queue.popleft()
    # print(v, end= ' ')
    
    for i in graph[v]:
        if not visited[i]:
            queue.append(i)
            visited[i] = True
            
answer = -1 # 감염 시작 컴퓨터는 제외
for visit in visited:
    if visit is True:
        answer += 1
print(answer)
