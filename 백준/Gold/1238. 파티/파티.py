import sys, heapq

n, m, x = map(int, sys.stdin.readline().split())

graph = [[] for _ in range(n + 1)]

for _ in range(m):
    a, b, c = map(int, sys.stdin.readline().split())
    
    graph[a].append([b, c]) # a->b, w
    
# start, dest = map(int, sys.stdin.readline().split())

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
    
# x에서 집가기
distance1 = dijkstra(x)
answer = 0

# i 에서 x가기 + 총합
for i in range(1, n+1):
    distance2 = dijkstra(i)
    answer = max(answer, distance1[i] + distance2[x])

print(answer)