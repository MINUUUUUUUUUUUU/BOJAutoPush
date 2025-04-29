from itertools import combinations
import copy

def dfs(graph, v, visited):
    visited[v[0]][v[1]] = True
    # print(v, end = ' ')
    for move in moves:
        pos = [v[0] + move[0], v[1] + move[1]]
        if pos[0] < 0 or pos[1] < 0 or pos[0] >= n or pos[1] >= m or graph[pos[0]][pos[1]] == 1 or graph[pos[0]][pos[1]] == 2:
            continue
        
        if not visited[pos[0]][pos[1]]:
            dfs(graph, pos, visited)

answer = 0

n, m = map(int, input().split())
lab = [list(map(int, input().split())) for i in range(n)]
# print(lab)

moves = [[-1, 0], [1, 0], [0, -1], [0, 1]]

visited = []
for i in range(n):
    visited.append([False for j in range(m)])

empty = []
virus = []
virus_count = 0

for i in range(n):
    for j in range(m):
        if lab[i][j] == 0:
            empty.append([i, j])
        if lab[i][j] == 2:
            virus.append([i, j])
            virus_count += 1
        if lab[i][j] == 1 or lab[i][j] == 2:
            visited[i][j] = True

# print(visited)

cases = list(combinations(empty, 3))

for case in cases:
    
    temp_lab = copy.deepcopy(lab)
    
    temp_lab[case[0][0]][case[0][1]] = 1
    temp_lab[case[1][0]][case[1][1]] = 1
    temp_lab[case[2][0]][case[2][1]] = 1
    
    # print(temp_lab)
    
    temp_visited = copy.deepcopy(visited)
    
    temp_visited[case[0][0]][case[0][1]] = True
    temp_visited[case[1][0]][case[1][1]] = True
    temp_visited[case[2][0]][case[2][1]] = True
    
    # dfs(temp_lab, virus[0], temp_visited)
   
    for i in range(virus_count):
        dfs(temp_lab, virus[i], temp_visited)
        # print()
    
    temp_count = 0
    for i in range(n):
        for j in range(m):
            if temp_visited[i][j] == False:
                temp_count += 1
    
    if temp_count >= answer:
        answer = temp_count

print(answer)
    