import sys, heapq

t = 1
while True:
    n = int(sys.stdin.readline())

    
    if n == 0:
        break
    
    board = list(list(map(int, sys.stdin.readline().split())) for _ in range(n))
    distance = [[1e9 for _ in range(n)] for _ in range(n)]
    distance[0][0] = board[0][0]
    
    queue = []
    heapq.heappush(queue, [board[0][0], 0, 0]) # dist, x, y
    
    dx = (0, 0, 1, -1)
    dy = (1, -1, 0, 0)
    
    while queue:
        dist, x, y = heapq.heappop(queue)
        if dist > distance[x][y]:
            continue
        
        for i in range(4):
            posx = x + dx[i]
            posy = y + dy[i]
            
            if posx < 0 or posy < 0 or posx > n-1 or posy > n-1:
                continue
            
            cost = dist + board[posx][posy]
            
            if distance[posx][posy] > cost:
                distance[posx][posy] = cost
                heapq.heappush(queue, [cost, posx, posy])
                
    
    print(f"Problem {t}: {distance[n-1][n-1]}")
    t += 1