def solution(N, stages):
    
    if N == 0:
        return [0]
    elif N == 1:
        return [1]
    
    ## N : 전체 스테이지 개수
    players = len(stages) ## 플레이어 수
    levels = [[i+1,0] for i in range(N)]
    print(levels)
    
    for j in stages:
        if j == N+1:
            continue
        levels[j-1][1] += 1 ##스테이지당 실패 횟수를 기록
    
    tmp = 0
    tmp2 = 0
    for l in range(N):
        tmp2 = levels[l][1]
        if (players - tmp) == 0:
            levels[l][1] = 0
            continue
        levels[l][1] = levels[l][1] / (players - tmp)
        tmp += tmp2
        
    levels.sort(key=lambda x:x[1], reverse=True)
    
    print(levels)
    answer = []
    for k in range(N):
        answer.append(levels[k][0])
    
    return answer