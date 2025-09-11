h, w = map(int, input().split())

blocks = list(map(int, input().split()))
# print(blocks)

answer = 0
max_left = blocks[0]
# max_right = blocks[-1]

for i in range(1, w-1):
    
    max_right = max(blocks[i+1:])
    
    if max_left > blocks[i] and max_right > blocks[i]:
        answer += min(max_left, max_right) - blocks[i]
    elif max_left < blocks[i]:
        max_left = blocks[i]
        
print(answer)