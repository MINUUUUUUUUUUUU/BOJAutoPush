def dfs(v):
    
    visited.add(v)

    # for i in graph[v]:
    i = 0
    for consulting in consultings[v[0]:]:
        
        tmp = (v[0] + i + consulting[0], v[1] + consulting[1])
        i += 1
        
        if tmp[0] > n:
            continue
        if tmp not in visited:
            dfs(tmp)
            

n = int(input())
consultings = []

for i in range(n):
    consultings.append(list(map(int, input().split())))
    
# print(consultings)

visited = set()

dfs((0, 0))

visited = list(visited)
# print(visited)
answer = 0
for i in visited:
    # print(i[1])
    if i[1] > answer:
        answer = i[1]

print(answer)