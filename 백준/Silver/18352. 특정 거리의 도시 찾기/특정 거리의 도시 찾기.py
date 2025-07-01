import sys, heapq

n, m, k, x = map(int, sys.stdin.readline().split())
graph = [[] for _ in range(n + 1)]

for _ in range(m):
    a, b = map(int, sys.stdin.readline().split())
    graph[a].append(b)

distance = [1e9 for _ in range(n+1)]
distance[x] = 0
queue = []
heapq.heappush(queue, [0, x])

while queue:
    dist, now = heapq.heappop(queue)
    
    if dist > distance[now]:
        continue
    
    for next in graph[now]:
        cost = dist + 1
        
        if distance[next] > cost:
            distance[next] = cost
            heapq.heappush(queue, [cost, next])
            
# print(distance)

if k not in distance:
    print(-1)
    exit()

for i in range(n+1):
    if distance[i] == k:
        print(i)
