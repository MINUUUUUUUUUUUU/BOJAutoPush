import sys
from itertools import permutations

n, m = map(int, sys.stdin.readline().split())
numbers = [a for a in range(1,n+1)]

cases = list(permutations(numbers, m))
cnt = 0
l = len(cases)
for case in cases:
    for c in case:
        print(c, end=' ')
    
    if not cnt == l-1:
        print()
    cnt += 1