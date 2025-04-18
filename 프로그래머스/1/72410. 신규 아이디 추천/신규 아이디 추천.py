def solution(new_id):
    answer = ''
    stack = []
    
    for c in list(new_id):
        
        # 1단계 new_id의 모든 대문자를 대응되는 소문자로 치환합니다.
        if c.isalpha():
            stack.append(c.lower())
        
        # 2단계
        if c.isdigit() or c == '-' or c == '_':
            stack.append(c)
        
        # 2단계, 3단계, 4단계
        if c == '.' and stack != []:
            if stack[-1] != '.':
                stack.append('.')
    
    # 5단계 new_id가 빈 문자열이라면, new_id에 "a"를 대입합니다.
    if stack == []:
        stack.append('a')
    
    # 6단계
    while len(stack) > 15:
        stack.pop()
    
    # 4단계
    if stack[-1] == '.':
        stack.pop()
    
    # 7단계
    while len(stack) <= 2:
        stack.append(stack[-1])
    
    answer = ''.join(stack)
    return answer