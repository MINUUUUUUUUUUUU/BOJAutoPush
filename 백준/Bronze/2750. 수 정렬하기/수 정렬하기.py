## 2750 수 정렬하기

n = int(input())
list = []
for i in range(n):
  list.append(int(input()))
list.sort()

for i in range(n):
  print(int(list[i]))