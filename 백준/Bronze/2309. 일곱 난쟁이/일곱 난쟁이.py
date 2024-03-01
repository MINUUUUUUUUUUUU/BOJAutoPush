## 2309 일곱 난쟁이

height=[]

for i in range(9):
  height.append(int(input()))

for n in range(9):
  for i in range(8):
    if height[i] > height[i+1]:
      temp = height[i]
      height[i] = height[i+1]
      height[i+1] = temp

i = 0
j = 0

while i < 9:
  j = 0
  while j < 9:
    if i == j:
      j += 1
      continue
    elif ((sum(height)-height[i]-height[j]) == 100):
      height.remove(height[i])
      height.remove(height[j-1])
      i = 100
      j = 100
    j += 1
  i += 1

for k in range(7):
  print(height[k])