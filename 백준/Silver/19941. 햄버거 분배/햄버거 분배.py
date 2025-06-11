import sys

n, k = map(int, sys.stdin.readline().split())
ham = list(map(str, sys.stdin.readline().strip()))
# print(ham)

answer = 0
for i in range(n):
    if ham[i] == 'P':
        isOk = 0
        for j in range(k, 0, -1):
            if i - j >= 0 and ham[i-j] == 'H':
                answer += 1
                ham[i-j] = 0
                isOk = 1
                break
        if isOk == 0:
            for j in range(1, k+1):
                if i + j < n and ham[i+j] == 'H':
                    answer += 1
                    ham[i+j] = 0
                    break
                

# print(ham)
print(answer)