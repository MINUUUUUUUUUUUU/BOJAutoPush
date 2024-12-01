n,k = map(int,input().split())
l = [i+1 for i in range(0,n)]
result = []
tmp = k

while l != []:
    while tmp > len(l):
        tmp = tmp - len(l)
    
    result.append(l[tmp-1])
    del l[tmp-1]
    tmp += k-1

print("<",end='')
print(*result,sep=', ',end='>')