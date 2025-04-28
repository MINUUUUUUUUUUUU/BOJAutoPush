from collections import deque

n = int(input())

r1, c1, r2, c2 = map(int, input().split())
if r1 == r2 and c1 == c2:
    print("0")
    exit()

visited = []
for i in range(n):
    visited.append([False for j in range(n)])
# print(visited)

queue = deque([[r1, c1, 0]]) # 0은 움직인 횟수
# print(queue)

visited[r1][c1] = True

# print(visited)

# (r-2, c-1), (r-2, c+1), (r, c-2), (r, c+2), (r+2, c-1), (r+2, c+1)
moves = [(-2, -1), (-2, 1), (0, -2), (0, 2), (2, -1), (2, 1)]

while queue:
    v = queue.popleft()
    # print(v, end = ' ')
    
    for move in moves:
        temp_position = [v[0] + move[0], v[1] + move[1], v[2] + 1]
        
        if temp_position[0] == r2 and temp_position[1] == c2:
            print(temp_position[2])
            exit()
        if temp_position[0] >= 0 and temp_position[0] < n and temp_position[1] >= 0 and temp_position[1] < n and not visited[temp_position[0]][temp_position[1]]:
            queue.append(temp_position)
            visited[temp_position[0]][temp_position[1]] = True
            
print("-1")