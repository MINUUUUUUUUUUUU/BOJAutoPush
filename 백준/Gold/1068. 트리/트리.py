import sys

n = int(sys.stdin.readline())

nodes = list(map(int,sys.stdin.readline().split()))
graph = [[] for _ in range(n)]
root = -1

# print(nodes)
for i in range(n):
    if nodes[i] == -1:
        root = i
    if nodes[i] >= 0:
        graph[nodes[i]].append(i)

# for i in range(n):
#     for j in graph[i]:
#         print(i, j)

die = int(sys.stdin.readline())

leaf_nodes = []

def dfs(v):
    if v == die:
        return
    
    if not graph[v]:
        leaf_nodes.append(v)
    
    for i in graph[v]:
        if i == die and len(graph[v]) == 1:
            leaf_nodes.append(v)
            break
        
        dfs(i)
    
dfs(root)
# print(leaf_nodes)
print(len(leaf_nodes))