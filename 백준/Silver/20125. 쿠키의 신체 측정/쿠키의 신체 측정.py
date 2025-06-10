import sys

n = int(sys.stdin.readline())

boards = tuple(tuple(sys.stdin.readline().strip()) for _ in range(n))

i = 0
while i < n:
    j = 0
    while j < n:
        # print(i, j)
        if boards[i][j] == '*':
            head = (i, j)
            heart = (i + 1, j)
            i = n
            j = n
        j += 1
    i += 1
    
# print(head)
# print(heart)

left_arm = 0
right_arm = 0
waist = 0

tmp = boards[heart[0]]

for i in range(1 , n):
    if heart[1] - i < 0 or tmp[heart[1] - i] != '*':
        break
    else:
        left_arm += 1

for i in range(1, n):
    if heart[1] + i >= n or tmp[heart[1] + i] != '*':
        break
    else:
        right_arm += 1

# print(left_arm)
# print(right_arm)

for i in range(1, n):
    if heart[0] + i >= n or boards[heart[0] + i][heart[1]] != '*':
        left_leg = (heart[0] + i, heart[1] - 1)
        right_leg = (heart[0] + i, heart[1] + 1)
        break
    else:
        waist += 1
# print(waist)
# print(left_leg)
# print(right_leg)
left_leg_len = 0
right_leg_len = 0

for i in range(0, n):
    if left_leg[0] + i >= n or boards[left_leg[0] + i][left_leg[1]] != '*':
        break
    else:
        left_leg_len += 1

for i in range(0, n):
    if right_leg[0] + i >= n or boards[right_leg[0] + i][right_leg[1]] != '*':
        break
    else:
        right_leg_len += 1
        
print(heart[0] + 1, heart[1] + 1)
print(left_arm, right_arm, waist, left_leg_len, right_leg_len)