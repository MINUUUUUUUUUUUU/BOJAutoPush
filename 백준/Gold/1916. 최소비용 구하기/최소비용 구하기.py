import sys, heapq

n = int(sys.stdin.readline())
m = int(sys.stdin.readline())

graph = [[] for _ in range(n + 1)]

for _ in range(m):
    a, b, c = map(int, sys.stdin.readline().split())
    
    graph[a].append([b, c]) # a->b, w
    
start, dest = map(int, sys.stdin.readline().split())

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
            
print(distance[dest])