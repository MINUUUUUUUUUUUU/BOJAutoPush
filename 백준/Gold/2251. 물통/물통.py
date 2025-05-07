import sys

a, b, c = map(int, sys.stdin.readline().split())

status = [[0, a], [0, b], [c,c]]
cases = set()
answer = set()
cases.add((0, 0, c))
# print(type((0, 0, c)))

def dfs(status):
    
    cases.add(status)
    # print(status)
    
    if status[0] == 0:
        answer.add(status[2])
        
    # A 물통을 옮길 때
    if status[0] != 0:
    
        # B로 옮길 때
        # A텅B
        if status[0] < b - status[1]:
            tmp = (0, status[0] + status[1], status[2])
            if tmp not in cases:
                dfs(tmp)
        else: # B꽉
            tmp = (status[0] - b + status[1], b, status[2])
            if tmp not in cases:
                dfs(tmp)
                
        # C로 옮길 때
        # A텅C
        if status[0] < c - status[2]:
            tmp = (0, status[1], status[0] + status[2])
            if tmp not in cases:
                dfs(tmp)
        else: # C꽉
            tmp = (status[0] - c + status[2], status[1], c)
            if tmp not in cases:
                dfs(tmp)
    
    # B 물통을 옮길 때    
    if status[1] != 0:
        # A로 옮길 때
        # B텅A
        if status[1] < a - status[0]:
            tmp = (status[0] + status[1], 0, status[2])
            if tmp not in cases:
                dfs(tmp)
        else: # A꽉
            tmp = (a, status[1] - a + status[0], status[2])
            if tmp not in cases:
                dfs(tmp)
    
        # C로 옮길 때
        # B텅C
        if status[1] < c - status[2]:
            tmp = (status[0], 0, status[1] + status[2])
            if tmp not in cases:
                dfs(tmp)
        else: # C꽉꽉
            tmp = (status[0], status[1] - c + status[2], c)
            if tmp not in cases:
                dfs(tmp)
                
    # C 물통을 옮길 때
    if status[2] != 0:
        # A로 옮길 때
        # C텅A
        if status[2] < a - status[0]:
            tmp = (status[0] + status[2], status[1], 0)
            if tmp not in cases:
                dfs(tmp)
        else: # A꽉
            tmp = (a, status[1], status[2] - a + status[0])
            if tmp not in cases:
                dfs(tmp)
        
        # B로 옮길 때
        # C텅B
        if status[2] < b - status[1]:
            tmp = (status[0], status[1] + status[2], 0)
            if tmp not in cases:
                dfs(tmp)
        else: # B꽉꽉
            tmp = (status[0], b, status[2] - b + status[1])
            if tmp not in cases:
                dfs(tmp)

dfs((0, 0, c))
tmp_answer = sorted(list(answer))
for i in tmp_answer:
    print(i, end=' ')
        