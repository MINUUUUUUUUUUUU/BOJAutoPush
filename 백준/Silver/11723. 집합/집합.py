import sys

S = set()

m = int(sys.stdin.readline())

for _ in range(m):

    tmp = sys.stdin.readline().split()
    if len(tmp) == 1:
        a = tmp[0]
    else:
        a = tmp[0]
        num = int(tmp[1])
    
    if a == 'add':
        S.add(int(num))
    elif a == 'remove':
        S.discard(int(num))
    elif a == 'check':
        if int(num) in S:
            print(1)
        else:
            print(0)
    elif a == 'toggle':
        if int(num) in S:
            S.discard(int(num))
        else:
            S.add(int(num))
    elif a == 'all':
        S = set([1,2,3,4,5,6,7,8,9,10,11,12,13,14,15,16,17,18,19,20])
    elif a == 'empty':
        S = set()