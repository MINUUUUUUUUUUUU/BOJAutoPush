from itertools import combinations

n = int(input())

players = [i for i in range(1, n+1)]
table = [input().split() for i in range(n)]
# print(table)

start_cases = list(combinations(players, n//2))
link_cases = [[] for i in range(len(start_cases))]


for i in range(len(start_cases)):
    for j in range(1, n+1):
        if j not in start_cases[i]:
            link_cases[i].append(j)
        
min_value = 100 * ( n ^ 2)

for sc, lc in zip(start_cases, link_cases):
    start_stat = 0
    link_stat = 0
    
    for i in sc:
        for j in sc:
            start_stat += int(table[i-1][j-1])
            
    for i in lc:
        for j in lc:
            link_stat += int(table[i-1][j-1])
            
         
    
    temp = abs(start_stat - link_stat)
    if temp < min_value:
        min_value = temp
        
print(min_value)
            