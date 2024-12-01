n = int(input())
k = int(input())

li = list(map(int,input().split()))

if n <= k:
  print(0)
  exit()
  
li.sort()
d = []

for i in range(n-1):
  d.append(li[i+1]-li[i])

d.sort()
print(sum(d[:n-k]))