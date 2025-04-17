from itertools import permutations

k = int(input())
signs = list(input().split())
numbers = [i for i in range(10)]

# print(signs)
# print(numbers)

cases = list(permutations(numbers, k+1))
answer_cases = []

for case in cases:
    
    flag = 1 # for문 마지막에서 그대로 1이면 성공
    # print(case)
    for i in range(len(case) - 1):
        if signs[i] is '<':
            if case[i] > case[i+1]:
                flag = 0
                break
        elif signs[i] is '>':
            if case[i] < case[i+1]:
                flag = 0
                break
                
    if flag == 1:
        answer_cases.append(int(''.join(map(str, case))))
        
print(str(max(answer_cases)).zfill(k+1)) 
print(str(min(answer_cases)).zfill(k+1))