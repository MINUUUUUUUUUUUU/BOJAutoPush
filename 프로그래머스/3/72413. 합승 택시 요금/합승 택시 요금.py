import heapq

def solution(n, s, a, b, fares):
    answer = 1e9
    
    graph = [[] for _ in range(n+1)]

    
    for u,v,w in fares:
        graph[u].append((v, w))
        graph[v].append((u, w))
        
    
    def dijkstra(start):
        queue = []
        distance = [1e9 for _ in range(n+1)]
        heapq.heappush(queue, [0, start])

        while queue:
            dist, now = heapq.heappop(queue)

            if dist > distance[now]:
                continue

            for next, w in graph[now]:
                cost = dist + w

                if distance[next] > cost:
                    distance[next] = cost
                    heapq.heappush(queue, [cost, next])
                    
        return distance
                
    ## 따로따로
    dis1 = dijkstra(s)
    answer = min(answer, dis1[a] + dis1[b])
    
    ## i까지 갔다가 쫑
    for i in range(1, n+1):
        
        if s == i:
            continue
            
        dis2 = dijkstra(s)
        dis3 = dijkstra(i)
        answer = min(answer, dis2[i] + dis3[a] + dis3[b])

    ## a or b를 들렀다 나머지 하나
    dis4 = dijkstra(s)
    dis5 = dijkstra(a)
    dis6 = dijkstra(b)
    
    answer = min(answer, dis4[a] + dis5[b], dis4[b] + dis6[a])
    
    return answer