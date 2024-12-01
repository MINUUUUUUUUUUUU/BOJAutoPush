n = int(input())

k = list(map(int,input().split())) ## 거리
l = list(map(int,input().split())) ## 리터당 가격
k.append(0)

cost = 0

for i in range(0,n):
    if i == 0:
        cost += k[i] * l[i]
        m = l[i]
        continue
    
    if m <= l[i]:
        cost += k[i] * m
    else:
        cost += k[i] * l[i]
        m = l[i]
        
print(cost)