def solution(mats, park):
    answer = 0
    mats.sort(reverse=True)
    
    for i in mats:
        for j in range(len(park)):
            for k in range(len(park[0])):
                tmp = 0
                
                if park[j][k] == '-1':
                    if int(i) == 1:
                        answer = 1
                        break
                    
                    if j+i > len(park) or k+i > len(park[0]):
                        continue
                        
                    for m in range(j, j+i):
                        for n in range(k, k+i):
                            if park[m][n] != '-1':
                                tmp = -1
                    if tmp != -1:
                        answer = i
                        
        if answer != 0:
            break
                        
    if answer == 0:
        answer = -1
    
    return answer