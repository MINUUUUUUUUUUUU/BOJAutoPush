def solution(prices):
    answer = [0 for i in range(len(prices))]
    
    stack = []
    
    for i in range(len(prices)):
          
        while stack != []:
            if prices[i] < prices[stack[-1]]:
                answer[stack[-1]] = i - stack[-1]
                stack.pop()
            else:
                break
                
        stack.append(i)
        
    while stack != []:
        tmp = stack.pop()
        answer[tmp] = len(prices) - tmp - 1
        
    return answer