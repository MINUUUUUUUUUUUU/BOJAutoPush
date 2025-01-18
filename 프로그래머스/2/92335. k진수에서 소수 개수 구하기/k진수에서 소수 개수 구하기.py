def solution(n, k):
    answer = 0
    
    rev_base = ''
    
    while n > 0:
        
        n, mod = divmod(n, k)
        rev_base += str(mod)
        
    rebase_list = rev_base[::-1].split('0')  
    
    for i in rebase_list:
        
        if i == '':
            continue
        
        check = 0
        tmp = int(i)
        
        if tmp < 2:
            continue
        
        for j in range(2, int(tmp**0.5) + 1): 
            if tmp % j == 0:
                check = 1
                break
                
        if check == 0:
            answer += 1
    
    print(answer)
    return answer