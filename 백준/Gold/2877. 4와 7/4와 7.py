k = int(input())

# 4 7 44 47 74 77 444 447 474 477 744 747 774 777
# 2개, 4개, 8개, 16개?

n = 0

while k > 0:
    n += 1
    k -= pow(2, n)
    
# print(n-1) # n-1 자릿수의 수인거야.
# print(k)
# print(n+k+1) # n-1 자릿수의 n+k+1 번째 수가 필요한 것이다!

answer = []
need = pow(2, n) + k
# print("need", need)

# while tmp <= 1:
tmp = pow(2, n)
# print("tmp", tmp)

while tmp > 1:
        
    tmp /= 2
    
    if need > tmp:
        answer.append(7)
        need -= tmp
    elif need == 0:
        answer.append(7)
    else:
        answer.append(4)
    
    
for a in answer:
    print(a, end='')


# case 8
# need 2 tmp 8

# 8 / 2 = 4 > 2 => '4'
# 4 / 2 = 2 > -2 => ''