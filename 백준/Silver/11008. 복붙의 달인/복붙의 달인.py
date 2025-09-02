t = int(input())

for _ in range(t):
    s, p = map(str, input().split())
    answer = 0
    
    ls = len(s)
    lp = len(p) 
    
    i = 0
    
    while i < ls:
        if i + lp <= ls and s[i:i+lp] == p:
            i += lp - 1
            
        i += 1
        answer += 1
        
    print(answer)
