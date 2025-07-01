import sys, heapq

n, m = map(int, sys.stdin.readline().split())

graph = [[] for _ in range(n + 1)]

for _ in range(m):
    a, b, c = map(int, sys.stdin.readline().split())
    
    graph[a].append([b, c]) # a->b, w
    graph[b].append([a, c]) # b->a, w
    
p1, p2 = map(int, sys.stdin.readline().split())

def dijkstra(start):
    distance = [1e9 for _ in range(n+1)]
    
    queue = []
    distance[start] = 0
    heapq.heappush(queue, [0, start])
    
    while queue:
        dist, now = heapq.heappop(queue)
        
        if dist > distance[now]:
            continue
        
        for next, w in graph[now]:
            cost = dist + w
            
            if cost < distance[next]:
                distance[next] = cost
                heapq.heappush(queue, [cost, next])
    
    return distance

answer = 0

case1 = 0    
case2 = 0

distance1 = dijkstra(1)
case1 += distance1[p1]
case2 += distance1[p2]

distance2 = dijkstra(p1)
distance3 = dijkstra(p2)

case1 += distance2[p2]
case2 += distance3[p1]

case1 += distance3[n]
case2 += distance2[n]

answer = min(case1, case2)

if answer >= 1e9:
    print(-1)
else:
    print(answer)