def solution(n, w, num):
    answer = 0
    s = [0 for i in range(w)]
    
    # 상자 적재
    for i in range(n):
        if i % (2 * w) >= w:
            s[w - (i%w) - 1] += 1
        else:
            s[(i%w)] += 1
        
    # 상자 꺼내기
    tmp = (num // w) - 1 if num % w == 0 else num // w
    
    if num % (2 * w) >= w:
        answer = s[w - (num % w) - 1] - tmp
    else:
         answer = s[(num % w) - 1] - tmp if num % w != 0 else s[0] - tmp
    
    return answer