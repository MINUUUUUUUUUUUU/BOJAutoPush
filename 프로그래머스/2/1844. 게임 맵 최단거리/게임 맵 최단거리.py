from collections import deque

def solution(maps):
    answer = 0
    n = len(maps)
    m = len(maps[0])
    visited = [[False for _ in range(m)] for _ in range(n)]
    
    direction = ((1, 0), (-1, 0), (0, 1), (0, -1))
    
    def bfs():
        queue = deque([(0, 0, 1)]) # X, Y, Count
        visited[0][0] = True
        
        while queue:
            v = queue.popleft()
            print(v, end=' ')
            
            for d in direction:
                pos = (v[0] + d[0], v[1] + d[1], v[2] + 1) # X, Y, Count
                
                if pos[0] < 0 or pos[1] < 0 or pos[0] > n-1 or pos[1] > m-1 or (maps[pos[0]][pos[1]] == 0):
                    continue
                
                if pos[0] == n-1 and pos[1] == m-1:
                    return pos[2]
                
                if not visited[pos[0]][pos[1]]:
                    queue.append(pos)
                    visited[pos[0]][pos[1]] = True
                    
        return -1
    
    return bfs()