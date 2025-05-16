from collections import deque

def solution(n, wires):
    answer = 101
    
    graph = [[] for i in range(n)]
    
    for a,b in wires:
        graph[a-1].append(b-1)
        graph[b-1].append(a-1)
        
    def bfs(start, a, b, visited):
        queue = deque([start])
        visited[start] = True
        cnt = 0

        while queue:
            v = queue.popleft()
            cnt += 1
            for i in graph[v]:
                if (v == a and i == b) or (v == b and i == a):
                    continue
                
                if not visited[i]:
                    queue.append(i)
                    visited[i] = True
        
        return cnt
    
    for a,b in wires:
        visited = [False for _ in range(n)]
        cases = []
        
        for i in range(n):
            if not visited[i]:
                cases.append(bfs(i, a-1, b-1, visited))
                
        if len(cases) == 2:
            tmp = abs(cases[0] - cases[1])
            if tmp < answer:
                answer = tmp
                      
    return answer