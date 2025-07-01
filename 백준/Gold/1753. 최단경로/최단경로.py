import heapq

v, e = map(int, input().split())
k = int(input())

graph = [[] for _ in range(v + 1)]

for _ in range(e):
    a, b, c = map(int, input().split())
    graph[a].append((b, c)) # a->b, w

distance = [1e9 for _ in range(v + 1)]
queue = []

distance[k] = 0
heapq.heappush(queue, [0, k])

# print(distance)

while queue:
    dist, now = heapq.heappop(queue)
    
    if distance[now] < dist:
        continue
    
    for next, w in graph[now]:
        cost = dist + w
        
        if distance[next] > cost:
            distance[next] = cost
            heapq.heappush(queue, [cost, next])
            
for i in range(1, v+1):
    if distance[i] == 1e9:
        print("INF")
    else:
        print(distance[i])