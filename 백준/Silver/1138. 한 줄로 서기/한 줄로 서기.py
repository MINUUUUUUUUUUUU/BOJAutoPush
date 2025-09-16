n = int(input())

info = list(map(int, input().split()))
line = [0 for _ in range(n)]

for i in range(n):
    
    cnt = 0
    
    for j in range(n):
        if cnt == info[i] and line[j] == 0:
            line[j] = i+1
            break
        
        if line[j] == 0:
            cnt += 1
    
# print(line)
for l in line:
    print(l, end=' ')