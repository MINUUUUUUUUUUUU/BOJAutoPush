def solution(n, s, a, b, fares):
    answer = 0
    
    graph = [[] for _ in range(n+1)]

    
    for u,v,w in fares:
        graph[u].append((v, w))
        graph[v].append((u, w))
    
    def smallest(distance, visited):
        min_val = 1e8
        index = 0
        for i in range(1, n+1):
            if distance[i] < min_val and not visited[i]:
                min_val = distance[i]
                index = i
        return index
        
    def dijkstra(start):
        visited = [False for _ in range(n+1)]
        distance = [1e8 for _ in range(n+1)]
        
        distance[start] = 0
        visited[start] = True
    
        for i in graph[start]:
            distance[i[0]] = i[1]
            
        for i in range(n-1):
            now = smallest(distance, visited)
            visited[now] = True
            
            for j in graph[now]:
                cost = distance[now] + j[1]
                if cost < distance[j[0]]:
                    distance[j[0]] = cost
                    
        return distance
    
    cases = set()
    
    ## 각자 집가는 경우
    tmp = dijkstra(s)
    cases.add(tmp[a] + tmp[b])
    
    # A or B 끼리 i까지 같이 가고 따로 집감
    for i in range(1, n+1):
        tmp_val = tmp[i]
        tmp2 = dijkstra(i)
        tmp_val += tmp2[a] + tmp2[b]
        cases.add(tmp_val)
    
    # print(cases)
    return min(cases)