n = int(input())
li = [i for i in map(int,input().split())]
li.sort()
m = 0

if n % 2 == 1:
  for i in range(n//2):
    if li[i] + li[-(i+2)] > m:
      m = li[i] + li[-(i+2)]
  if li[-1] > m:
    m = li[-1]
  
elif n % 2 == 0:
  for i in range(n//2):
    if li[i] + li[-(i+1)] > m:
      m = li[i] + li[-(i+1)]

print(m)