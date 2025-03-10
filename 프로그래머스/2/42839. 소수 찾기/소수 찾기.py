import itertools

def is_prime(num):
    if num==0 or num==1:
        return 0
    elif num==2:
        return 1
    
    for i in range(2,num):
        if num%i == 0:
            return 0 #소수가 아니면
    return 1 #소수면

def solution(numbers):
    answer = []
    numbers = list(numbers)
    print(numbers)
    
    for r in range(1, len(numbers) + 1):
        for perm in itertools.permutations(numbers, r):
            tmp = int(''.join(perm))
            if is_prime(tmp):
                if tmp not in answer:
                    answer.append(tmp)
    
    return len(answer)