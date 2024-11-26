
t = int(input())

for _ in range(t):
  n = int(input())
  a = list(map(int, input().split()))
  profit = 0
  m = 0

  for i in range(n-1,-1,-1):
    if a[i] > m:
      m = a[i]
    else:
      profit += m - a[i]
    
  print(profit)