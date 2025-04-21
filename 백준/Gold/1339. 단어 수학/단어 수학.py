## 1339: 단어 수학

from itertools import permutations

n = int(input())
words = [input() for i in range(n)]

alphabets = {}

for word in words:
    for i in range(len(word)):
        if word[i] in alphabets:
            alphabets[word[i]] += 10 ** (len(word) - (i+1))
            continue
        alphabets[word[i]] = 10 ** (len(word) - (i+1))

# print(alphabets)

sorted_alphabets = sorted(alphabets.items(), key=lambda x: x[1], reverse=True)
max_value = 0

temp_i = 0

# print(sorted_alphabets[0][1])

for i in range(9, -1, -1):
    if temp_i < len(sorted_alphabets):
        max_value += sorted_alphabets[temp_i][1] * i
        temp_i += 1
    
print(max_value)