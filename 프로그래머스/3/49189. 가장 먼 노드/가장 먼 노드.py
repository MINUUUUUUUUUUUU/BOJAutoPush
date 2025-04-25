from collections import deque

distance = {}

def solution(n, edge):
    answer = 0
    g = [[] for i in range(n)]
    for a, b in edge:
        g[a-1].append(b-1)
        g[b-1].append(a-1)
    
    # print(g)
    visited = [False for i in range(n)]
    
    bfs(g, 0, visited)
    
    max_value = max(distance.values())
    for v in distance.values():
        if v == max_value:
            answer += 1
        
    print(distance)
    
    return answer

def bfs(graph, start, visited):
    
    queue = deque([start])
    visited[start] = True
    distance[start] = 0
    
    while queue:
        v = queue.popleft()
        # print(v+1, end= ' ')

        for i in graph[v]:
            if not visited[i]:
                queue.append(i)
                visited[i] = True
                distance[i] = distance[v] + 1
        # print()