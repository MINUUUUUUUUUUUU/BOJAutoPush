import sys

n, m = map(int, sys.stdin.readline().split())

graph = [[False for i in range(n)] for j in range(n)]

for _ in range(m):
    a, b = map(int, sys.stdin.readline().split())
    graph[a-1][b-1] = True
    
visited = [False for i in range(n)]

def dfs(graph, v, visited):
    
    if visited[v]:
        return;
    
    for i in range(n):
        if graph[v][i] is True:
            dfs(graph, i, visited)
            for j in range(n):
                if not graph[v][j] or graph[i][j]:
                    graph[v][j] = graph[i][j];
    visited[v] = True
    
answer = 0

for i in range(n):
    if visited[i]:
        continue
    dfs(graph, i, visited)

for i in range(n):
    tmp = 0
    for j in range(n):
        if graph[i][j] or graph[j][i]:
            tmp += 1
    if tmp == n-1:
        answer += 1
        
print(answer)