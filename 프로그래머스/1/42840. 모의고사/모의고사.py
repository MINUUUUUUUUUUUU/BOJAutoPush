def solution(answers):
    
    check = [0, 0, 0]
    for i in range(len(answers)):
        #1번 수포자
        if ((i+1)%5) == answers[i] % 5:
            check[0] += 1
        
        #2번 수포자
        if i%2 == 0:
            if answers[i] == 2:
                check[1] += 1
        elif i%2 == 1:
            if i%8 == 1:
                if answers[i] == 1:
                    check[1] += 1
            elif i%8 == 3:
                if answers[i] == 3:
                    check[1] += 1
            elif i%8 == 5:
                if answers[i] == 4:
                    check[1] += 1
            elif i%8 == 7:
                if answers[i] == 5:
                    check[1] += 1
        
        #3번 수포자
        if i%10 == 0 or i%10 == 1:
            if answers[i] == 3:
                check[2] += 1
        elif i%10 == 2 or i%10 == 3:
            if answers[i] == 1:
                check[2] += 1
        elif i%10 == 4 or i%10 == 5:
            if answers[i] == 2:
                check[2] += 1
        elif i%10 == 6 or i%10 == 7:
            if answers[i] == 4:
                check[2] += 1
        elif i%10 == 8 or i%10 == 9:
            if answers[i] == 5:
                check[2] += 1
            
    print(check)
    
    result = []
    tmp = max(check)
    for j in range(3):
        if check[j] == tmp:
            result.append(j+1)
    
    
    return result