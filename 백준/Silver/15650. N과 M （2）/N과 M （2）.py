from itertools import combinations

n, m = map(int, input().split())

numbers = [i for i in range(1, n+1)]
cases = list(combinations(numbers, m))

l = len(cases)
t = 0

for case in cases:
    
    k = 0
    for c in case:
        
        if k == m-1:
            print(c, end='')
            break
        
        print(c, end =' ')
        k += 1
    
    if t == l-1:
        break
    
    print()
    t += 1