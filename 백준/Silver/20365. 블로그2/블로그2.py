n = int(input())
str = input()
b_count, r_count = 0, 0
for i in range(n):
  if i == 0:
    if str[i] == 'B':
      b_count += 1
    if str[i] == 'R':
      r_count += 1
  
  if str[i] == 'B' and str[i-1] == 'B':
    continue
  elif str[i] == 'R' and str[i-1] == 'R':
    continue
  
  if str[i] == 'B':
    b_count += 1
  if str[i] == 'R':
    r_count += 1

print (min(b_count,r_count) + 1)