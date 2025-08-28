def solution(citations):
    answer = 0
    
    n = len(citations)
    citations.sort()
    # print(citations)
    
    for i in range(n):
        if n - i<= citations[i]:
            answer = n - i
            break
    
    return answer