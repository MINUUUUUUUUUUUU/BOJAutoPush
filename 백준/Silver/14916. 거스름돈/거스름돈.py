n = int(input())
count = 0
end = 0

if n < 5 and n % 2 != 0:
  print(-1)
  end = 1

if n % 5 == 0:
  count += n // 5
  n %= 5
elif ( n % 5 ) % 2 == 0:
  count += ( n // 5 )
  n %= 5
  count += ( n // 2 )
  n %= 2
else:
  count += ( n // 5 ) - 1
  n = n % 5 + 5
  count += ( n // 2 )
  n %= 2

if end != 1:
  print(count)