from collections import deque

n, m = map(int, input().split())

board = [[-1 for i in range(m + 2)]] # -1은 공기, 0은 빈 땅, 1은 치즈, 2는 녹을 치즈
for i in range(n):
    
    tmp_list = [-1]
    for t in list(map(int, input().split())):
        tmp_list.append(t)
    tmp_list.append(-1)
    
    board.append(tmp_list)

board.append([-1 for i in range(m + 2)])

# print(board)

direction = [[-1, 0], [1, 0], [0, 1], [0, -1]]

def bfs(graph, start, visited):
    queue = deque([start])
    visited[start[0]][start[1]] = True
    
    while queue:
        v = queue.popleft()
        
        for d in direction:
            pos = [ v[0] + d[0] , v[1] + d[1] ]
            if pos[0] < 0 or pos[1] < 0 or pos[0] > n+1 or pos[1] > m+1: #보드를 벗어났을 때
                continue
            
            if not visited[pos[0]][pos[1]]:
                if graph[pos[0]][pos[1]] == 1:
                    graph[pos[0]][pos[1]] = 2
                    continue
                elif graph[pos[0]][pos[1]] == 0 or graph[pos[0]][pos[1]] == -1:
                    visited[pos[0]][pos[1]] = True
                    queue.append(pos)

visited = [[False for i in range(m+2)] for j in range(n+2)]
cnt = 0

while True:
    
    flag = 0
    for b in board:
        if 1 in b:
            flag = 1
            break
    
    if flag == 0:
        break
    
    cnt += 1
    
    for i in range(n+2):
        for j in range(m+2):
            if board[i][j] == -1 and not visited[i][j]:
                bfs(board, [i,j], visited)
            
    temp_sum = 0    
    for i in range(n+2):
        for j in range(m+2):
            if board[i][j] == 2:
                board[i][j] = -1
                temp_sum += 1
            


# print(board)
print(cnt)
print(temp_sum)