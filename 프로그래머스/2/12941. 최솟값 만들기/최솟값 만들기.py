def solution(A,B):
    answer = 0

    A.sort()
    B.sort(reverse=True)
    l = len(A)
    
    
    for i in range(l):
        answer += A[-1] * B[-1]
        A.pop()
        B.pop()

    return answer