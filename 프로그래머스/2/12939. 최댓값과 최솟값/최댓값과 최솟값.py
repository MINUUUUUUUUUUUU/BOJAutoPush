def solution(s):
    answer = ''
    l = list(map(int,s.split()))
    # print(l)
    answer = str(min(l)) + " " + str(max(l))
    return answer