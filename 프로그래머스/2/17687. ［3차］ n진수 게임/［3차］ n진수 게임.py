def transform(num, base):
    result = ''
    
    while num > 0:
        num, m = divmod(num, base)
        if m >= 10:
            result += chr(m + 55)
        else:
            result += str(m)
    
    return result[::-1]

def solution(n, t, m, p):
    answer = ''
    
    # print(transform(10, 2))
    game = '0'
    for i in range(1, t * m):
        game += str(transform(i, n))
    # print(game)
    
    for i in range(t * m):
        if i % m == (p-1):
            # print(game[i], end=' ')
            answer += game[i]
    
    return answer