import sys
import copy

n, l = map(int, sys.stdin.readline().split())

maps = tuple(tuple(map(int,sys.stdin.readline().split())) for _ in range(n))
# print(maps)
lines = []
lines2 = [[] for _ in range(n)]
for m in maps:
    lines.append(list(m))
    for i in range(n):
        lines2[i].append(m[i])

tmp = copy.deepcopy(lines)
lines.extend(lines2)
lines = tuple(lines)
lines2.extend(tmp)
lines2 = tuple(lines2)
# print(lines)
# print(lines2)

answer1 = 0
k = 0

for line in lines:
    flag = 1 # 1 상태면 answer += 1
    stairs = set()
    for i in range(1, n):
        if line[i] != line[i-1]: # 1부터 시작해서 index 안남
            if line[i] == line[i-1] + 1: # 오른쪽 부분이 1칸 더 높으면
                if i - 1 - l + 1 < 0:
                    flag = 0
                else:
                    if k > n-1:
                        for j in range(l):
                            if line[i-1 - j] != line[i-1] or (i-1-j, k) in stairs:
                                flag = 0
                        if flag == 1:
                            for j in range(l):
                                stairs.add( tuple([ i- 1 - j, k ]) )
                    else:
                        for j in range(l):
                            if line[i-1 - j] != line[i-1] or (k, i-1-j) in stairs:
                                flag = 0
                        if flag == 1:
                            for j in range(l):
                                stairs.add( tuple([k, i- 1 - j]) )
            elif line[i] == line[i-1] - 1: # 왼쪽 부분이 1칸 더 높으면
                if i + l - 1 > n-1:
                    flag = 0
                else:
                    if k > n-1:
                        for j in range(l):
                            if line[i + j] != line[i] or (i+j, k) in stairs:
                                flag = 0
                        if flag == 1:
                            for j in range(l):
                                stairs.add( tuple([i + j, k]) )
                    else:
                        for j in range(l):
                            if line[i + j] != line[i] or (k, i+j) in stairs:
                                flag = 0
                        if flag == 1:
                            for j in range(l):
                                stairs.add( tuple([k, i + j]) )
            else:
                flag = 0
    if flag == 1:
        # print(line)
        answer1 += 1
    k += 1 # 몇번째 라인인지지

################################ 세로 먼저 ##########################################
answer2 = 0
k = 0

for line in lines2:
    stairs = set()
    flag = 1 # 1 상태면 answer += 1
    for i in range(1, n):
        if line[i] != line[i-1]: # 1부터 시작해서 index 안남
            if line[i] == line[i-1] + 1: # 오른쪽 부분이 1칸 더 높으면
                if i - 1 - l + 1 < 0:
                    flag = 0
                else:
                    if k <= n-1:
                        for j in range(l):
                            if line[i-1 - j] != line[i-1] or (i-1-j, k) in stairs:
                                flag = 0
                            else:
                                stairs.add( tuple([ i- 1 - j, k ]) )
                    else:
                        for j in range(l):
                            if line[i-1 - j] != line[i-1] or (k, i-1-j) in stairs:
                                flag = 0
                            else:
                                stairs.add( tuple([k, i- 1 - j]) )
            elif line[i] == line[i-1] - 1: # 왼쪽 부분이 1칸 더 높으면
                if i + l - 1 > n-1:
                    flag = 0
                else:
                    if k <= n-1:
                        for j in range(l):
                            if line[i + j] != line[i] or (i+j, k) in stairs:
                                flag = 0
                            else:
                                stairs.add( tuple([i + j, k]) )
                    else:
                        for j in range(l):
                            if line[i + j] != line[i] or (k, i+j) in stairs:
                                flag = 0
                            else:
                                stairs.add( tuple([k, i + j]) )
            else:
                flag = 0
    if flag == 1:
        # print(line)
        answer2 += 1
    k += 1 # 몇번째 라인인지

# print(stairs)
# print(answer1)
# print(answer2)
print(max(answer1, answer2))