## 1085 직사각형에서 탈출

x,y,w,h = map(int,input().split())
result = x
if result > y: result = y
if result > w-x: result = w-x
if result > h-y: result = h-y

print(result)