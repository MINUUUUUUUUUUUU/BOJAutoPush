from collections import deque

t = int(input())
directions = [[1, 2], [2, 1], [2, -1], [1, -2], [-1, -2], [-2, -1], [-2, 1], [-1, 2]]

def bfs(start, visited, n, goal):
    queue = deque([[start, 0]])
    # print(queue[0])
    visited[start[0]][start[1]] = True
    
    while queue:
        v = queue.popleft()
        # print(v, end= ' ')
        
        for d in directions:
            pos = [ [ v[0][0] + d[0] , v[0][1] + d[1] ] , v[1] + 1 ]
            if pos[0][0] < 0 or pos[0][1] < 0 or pos[0][0] > n-1 or pos[0][1] > n-1:
                continue
            if pos[0] == goal:
                return pos[1]
            if not visited[pos[0][0]][pos[0][1]]:
                queue.append(pos)
                visited[pos[0][0]][pos[0][1]] = True
        
    
for _ in range(t):
    n = int(input())
    visited = [[False for _ in range(n)] for _ in range(n)]
    start_point = list(map(int,input().split()))
    end_point = list(map(int,input().split()))
    
    if start_point == end_point:
        print(0)
        continue
    
    print(bfs(start_point, visited, n, end_point))