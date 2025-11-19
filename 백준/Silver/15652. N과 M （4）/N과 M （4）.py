n, m = map(int, input().split())

numbers = [i for i in range(1, n+1)]
# print(numbers)

cases = []

def backtracking(case, k, v):
    if k == m:
        # print(case)
        case.sort()
        
        print(' '.join(map(str,case)))
        
        return
    
    for num in numbers:
        if num < v:
            continue
        case.append(num)
        backtracking(case, k + 1, max(v, num))
        case.pop()
        
backtracking([], 0, 0)
# print(cases)