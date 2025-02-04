def solution(s):
    answer = True
    
    stack = []
    for i in s:
        if i == '(':
            stack.append('1')
        else:
            if '1' not in stack:
                answer = False
            else:
                stack.pop()

    if '1' in stack:
        answer = False
    return answer