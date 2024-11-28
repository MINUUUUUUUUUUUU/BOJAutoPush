n = int(input())
li = [list(map(int,input().split())) for _ in range(n)]
li.sort(key=lambda x:(x[1],x[0]))
tmp = 0
cnt = 0

for i in li:
  if tmp <= i[0]:
    tmp = i[1]
    cnt += 1

print(cnt)