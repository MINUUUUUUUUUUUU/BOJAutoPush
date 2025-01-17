def solution(survey, choices):
    answer = ''
    mbti = [0, 0, 0, 0] #양수면 각각 R,C,J,A 음수면 각각 T,F,M,N
    
    for i, k in zip(survey, choices):
        
        if 'R' in i:
            if i[0] == 'R':
                mbti[0] -= int(k) - 4
            elif i[0] == 'T':
                mbti[0] += int(k) - 4
        if 'C' in i:
            if i[0] == 'C':
                mbti[1] -= int(k) - 4
            elif i[0] == 'F':
                mbti[1] += int(k) - 4
        if 'J' in i:
            if i[0] == 'J':
                mbti[2] -= int(k) - 4
            elif i[0] == 'M':
                mbti[2] += int(k) - 4
        if 'A' in i:
            if i[0] == 'A':
                mbti[3] -= int(k) - 4
            elif i[0] == 'N':
                mbti[3] += int(k) - 4
    
    print(mbti)
    answer_temp = []
    
    if mbti[0] >= 0: 
        answer_temp.append('R')
    else:
        answer_temp.append('T')
    
    if mbti[1] >= 0: 
        answer_temp.append('C')
    else:
        answer_temp.append('F')
    
    if mbti[2] >= 0: 
        answer_temp.append('J')
    else:
        answer_temp.append('M')
        
    if mbti[3] >= 0: 
        answer_temp.append('A')
    else:
        answer_temp.append('N')
        
    answer = ''.join(answer_temp)
    return answer