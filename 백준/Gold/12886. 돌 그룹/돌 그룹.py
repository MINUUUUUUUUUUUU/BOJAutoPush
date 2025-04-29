from collections import deque
import copy
import sys

def bfs(start):
    
    if start[0] == start[1] and start[1] == start[2]:
        return 1
    
    queue = deque([start])
    
    visited = set()
    visited.add(tuple(sorted(start)))
    
    while queue:
        a = queue.popleft()
    
        for i, j in ((0,1), (0,2), (1,2)):
            v = copy.deepcopy(a)
            
            if v[i] == v[j]:
                continue
            
            if v[i] > v[j]:
                v[i] -= v[j]
                v[j] += v[j]
            else:
                v[j] -= v[i]
                v[i] += v[i]
            
            if v[0] == v[1] and v[1] == v[2]:
                return 1
            
            # print(visited)    
            
            if tuple(sorted(v)) not in visited:
                queue.append(v)
                visited.add(tuple(sorted(v)))
                
    return 0
    
a, b, c = map(int, sys.stdin.readline().split())

print(bfs([a,b,c]))
