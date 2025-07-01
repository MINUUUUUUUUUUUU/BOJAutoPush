import sys, heapq

m, n = map(int, sys.stdin.readline().split())

maze = list(list(map(int, sys.stdin.readline().strip())) for _ in range(n))
# print(maze)

distance = [[1e9 for _ in range(m)] for _ in range(n)]
distance[0][0] = 0

queue = []
heapq.heappush(queue, [0, 0, 0]) # 부순 횟수, x, y
# visited = [[False for _ in range(m)] for _ in range(n)]

while queue:
    dist, x, y = heapq.heappop(queue)
    
    if dist > distance[x][y]:
        continue
    
    ## x+1, y
    if x+1 < n and dist + maze[x+1][y] < distance[x+1][y]:
        distance[x+1][y] = dist + maze[x+1][y]
        heapq.heappush(queue, [dist+ maze[x+1][y], x+1, y])
    
    ## x, y+1
    if y+1 < m and dist + maze[x][y+1] <+ distance[x][y+1]:
        distance[x][y+1] = dist + maze[x][y+1]
        heapq.heappush(queue, [dist+maze[x][y+1], x, y+1])
    
    ## x-1, y
    if x-1 >= 0 and dist + maze[x-1][y] < distance[x-1][y]:
        distance[x-1][y] = dist + maze[x-1][y]
        heapq.heappush(queue, [dist+maze[x-1][y], x-1, y])
    
    ## x, y-1
    if y-1 >= 0 and dist + maze[x][y-1] < distance[x][y-1]:
        distance[x][y-1] = dist + maze[x][y-1]
        heapq.heappush(queue, [dist+maze[x][y-1] , x, y-1])
        
print(distance[n-1][m-1])