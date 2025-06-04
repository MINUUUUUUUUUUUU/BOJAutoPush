global answer
answer = 0

def solution(numbers, target):
    
    sign = (-1, 1)
    
    def recursive(num, i):
        global answer
        if num == target and i == len(numbers):
            answer += 1
                
        if i > len(numbers) - 1:
            return
        
        for s in sign:
            num += s * numbers[i]
            i += 1
            recursive(num, i)
            i -= 1
            num -= s * numbers[i]
        
    recursive(0, 0)
    return answer