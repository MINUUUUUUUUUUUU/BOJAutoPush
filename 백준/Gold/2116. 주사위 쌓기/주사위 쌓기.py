n = int(input())

# 위아래 관계 (인덱스)
# A - F (0-5)
# B - D (1-3)
# C - E (2-4)

dices = list(list(map(int, input().split())) for _ in range(n))
# print(dices)

answer = 0

def find_index(k):
    if k == 0:
        return 5
    
    if k == 1:
        return 3
        
    if k == 2:
        return 4
        
    if k == 3:
        return 1
        
    if k == 4:
        return 2
    
    if k == 5:
        return 0

answer = 0

for start in range(6):
    check = dices[0][start]
    
    s = 0
    for ii in range(6):
        if ii == start or ii == find_index(start):
            continue
        s = max(s, dices[0][ii])
        
    
    for i in range(1, n):
        for j in range(6):
            if dices[i][j] == check:
                t = find_index(j)
                
                m = 0
                
                for iii in range(6):
                    if iii == j or iii == t:
                        continue
                    m = max(m, dices[i][iii])
                
                s += m
                check = dices[i][t]
                break
                
    answer = max(answer, s)

print(answer)