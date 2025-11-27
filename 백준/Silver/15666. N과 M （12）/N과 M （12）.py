from itertools import combinations_with_replacement

n, m = map(int, input().split())
numbers = list(map(int, input().split()))

numbers.sort()
answers = set(combinations_with_replacement(numbers, m))

# print(answers)

for a in answers:
    print(' '.join(map(str, a)))