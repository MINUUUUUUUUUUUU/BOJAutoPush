visited = []

def solution(n, computers):
    answer = 0

    status = [[] for j in range(n)]
    
    for i in range(n):
        for j in range(n):
            if i == j:
                continue            
            if computers[i][j] == 1:
                status[i].append(j)
                
    visited = [False for i in range(n)]
    
    
    c = 0
    while c < n:
        if visited[c] is False:
            dfs(status, c, visited)
            answer += 1
        if visited[c] is True:
            c += 1
            
    
    return answer

def dfs(graph, i, visited):
    visited[i] = True
    print(i, end = ' ')
    
    for k in graph[i]:
        if not visited[k]:  
            dfs(graph, k, visited)