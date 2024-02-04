## 4375 1

while True:
  try:
     n = int(input())
     result = 1

     while True:
       if result % n == 0:
         break
       result = result * 10 + 1

     print(len(str(result)))
  except:
    break