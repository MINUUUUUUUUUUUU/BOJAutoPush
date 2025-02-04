def dfs(graph, v, visited):
    visited[v] = True
    print(v, end=' ')
    for i in graph[v]:
        if not visited[i]:
            dfs(graph, i, visited)
            
from collections import deque

def bfs(graph, start, visited):
    queue = deque([start])
    visited[start] = True
    while queue:
        v = queue.popleft()
        print(v,end=' ')
        for i in graph[v]:
            if not visited[i]:
                queue.append(i)
                visited[i] = True
    

n, m, v = map(int, input().split())
g = [[] for i in range(n+1)]
for i in range(m):
    a, b = map(int,input().split())
    g[a].append(b)
    g[b].append(a)

for i in range(1,n+1):
    g[i].sort()
    
visited = [False] * (n+1)
dfs(g, v, visited)

print()
visited = [False] * (n+1)
bfs(g, v, visited)