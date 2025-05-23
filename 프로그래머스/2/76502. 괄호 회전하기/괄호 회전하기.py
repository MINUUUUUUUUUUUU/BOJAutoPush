from collections import deque
import copy

def solution(s):
    answer = 0
    l = len(s)
    queue = deque(s)
    # print(queue)
    
    def check(q): # 올바른 괄호인지 체크하는 함수
        # print(queue)
        # print(q)
        stack = []
        # q.popleft()
        while q:
            c = q.popleft()
            # print(c, end=' ')
            if c == '(':
                stack.append(')')
            elif c == '{':
                stack.append('}')
            elif c == '[':
                stack.append(']')
            
            if c == ')':
                if stack == [] or c != stack[-1]:
                    return False
                stack.pop()
            elif c == '}':
                if stack == [] or c != stack[-1]:
                    return False
                stack.pop()
            elif c == ']':
                if stack == [] or c != stack[-1]:
                    return False
                stack.pop()
        
        if stack == []:
            return True
        return False
            
    for _ in range(l):
        c = queue.popleft()
        queue.append(c)
        qq = copy.deepcopy(queue)
        # print(qq)
        if check(qq):
            answer += 1
        # print()
        
    return answer