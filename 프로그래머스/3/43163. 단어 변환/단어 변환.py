from collections import deque

def solution(begin, target, words):
    answer = 0
    
    if target not in words:
        return 0
    
    words.append(begin)
    # print(words)
    l = len(words)
    # print(l)
    graph = [[] for _ in range(l)]
    for i in range(l):
        for j in range(i+1, l):
            # print(words[j], end= ' ')
            for k in range(len(words[i])):
                if (words[i][:k] == words[j][:k]) and (words[i][k+1:] == words[j][k+1:]): # ~:k-1 + k+1:~
                    # print(words[i], words[j])
                    graph[i].append(j)
                    graph[j].append(i)
        # print()
                    
    print(graph)            
    
    visited = [False for _ in range(len(words))]
    # answer = dfs(len(words) - 1, visited, 0)
    
    queue = deque([(l-1, 0)]) # index, count
    visited[l-1] = True
    
    while queue:
        v = queue.popleft()
        print(v, end= ' ')
        if words[v[0]] == target:
            return v[1]
        
        for i in graph[v[0]]:
            if not visited[i]:
                queue.append((i, v[1] + 1))
                visited[i] = True
                
    # print(visited)
    return answer