## 로또는 1~49
## 에서 6개를 골라야함

from itertools import combinations

k = -1

while k != 0:
    temp_list = input().split()
    k = temp_list[0]
    if int(k) == 0:
        break
    numbers = temp_list[1:]
    combi = list(combinations(numbers, 6))
    for comb in combi:
        for com in comb:
            print(com, end=' ')
        print()
    print()