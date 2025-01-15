def solution(friends, gifts):
    answer = 0
    ix = [0 for i in range(len(friends))]
    
    t = 0
    
    # 선물 지수
    for i in friends:
        
        for j in gifts:
            a,b = j.split() #a는 선물을 준 친구 #b는 선물을 받은 친구
            if a == i:
                ix[t] += 1
            if b == i:
                ix[t] -= 1    
        t += 1
    
    max = 0
    
    for i in range(len(friends)):
        cnt = [0 for tmp_var in range(len(friends))]
        
        for j in gifts:
            a, b = j.split()
            if a == friends[i]:
                n = friends.index(b)
                cnt[n] += 1
            if b == friends[i]:
                n = friends.index(a)
                cnt[n] -= 1
        
        m = 0
        g = 0
        while m < len(friends):
            if m == i:
                m += 1
                continue
            elif cnt[m] > 0:
                g += 1
            elif cnt[m] == 0:
                if ix[m] < ix[i]:
                    g += 1
            m += 1
            
        if max < g:
            max = g
                
                
    answer = max
    return answer