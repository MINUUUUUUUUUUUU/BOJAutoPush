from itertools import combinations_with_replacement

n = int(input())
numbers = set()

iter = [1, 5, 10, 50]
for i in combinations_with_replacement(iter, n):
    numbers.add(sum(i))
    # print(sum(i))

# print(numbers)
print(len(numbers))