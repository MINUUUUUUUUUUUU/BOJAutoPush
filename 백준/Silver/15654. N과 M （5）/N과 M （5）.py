from itertools import permutations

n, m = map(int, input().split())
numbers = list(map(int, input().split()))

numbers.sort()

answers = list(permutations(numbers, m))
for answer in answers:
    print(' '.join(map(str, answer)))