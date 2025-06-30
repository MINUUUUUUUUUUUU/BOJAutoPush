import sys, heapq

n, k = map(int, sys.stdin.readline().split())

if k == 0:
    print(n)
    exit()

distance = [1e9 for _ in range(max(2 * n + 1, 2 * k + 1))]
queue = []

distance[n] = 0
heapq.heappush(queue, (0, n))

while queue:
    dist, now = heapq.heappop(queue)
    
    if distance[now] < dist:
        continue
    
    # 현재 위치가 크면 -1
    if now > 0 and dist + 1 < distance[now - 1]:
            distance[now - 1] = dist + 1
            heapq.heappush(queue, (dist+1 , now-1) )
    
    # 현재 위치가 작으면 +1
    if now + 1 < len(distance) and dist + 1 < distance[now + 1]:
            distance[now + 1] = dist + 1
            heapq.heappush(queue, (dist + 1, now + 1))

    if now * 2 < len(distance):
        if dist < distance[now * 2]:
            distance[now * 2] = dist
            heapq.heappush(queue, (dist, now * 2))

# print(distance)
print(distance[k])