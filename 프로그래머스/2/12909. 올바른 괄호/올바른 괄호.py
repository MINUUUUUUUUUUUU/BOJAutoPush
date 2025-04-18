def solution(s):
    answer = True
    
    stack = []
    
    for e in s:
        if e == '(':
            stack.append(')')
        elif e == ')':
            if stack == []:
                return False
            stack.pop()

    if not stack == []:
        return False
    return True