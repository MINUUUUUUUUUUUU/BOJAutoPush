import sys
from collections import deque

n, m, x, y, ks = map(int, sys.stdin.readline().split()) # N=세로, M=가로

maps = list(list(map(int, sys.stdin.readline().split())) for _ in range(n))
# print(maps) #요소는 10미만의 자연수 또는 0

# 동쪽은 1, 서쪽은 2, 북쪽은 3, 남쪽은 4
cmd = tuple(map(int, sys.stdin.readline().split())) #명령어

dx = (0, 0, -1, 1) #동서북남 순 
dy = (1, -1, 0, 0) #동서북남 순

queue = deque([(x, y)])

dice = [0, 0, 0, 0, 0, 0]

#   1
# 3 0 2
#   4
#   5
# 해당 코드에선 모두 0이 윗면을 바라보는 모습으로 가정

# 동쪽으로~
def move_right():
    tmp = dice[0]
    dice[0] = dice[3]
    dice[3] = dice[5]
    dice[5] = dice[2]
    dice[2] = tmp
    
# 서쪽으로~
def move_left():
    tmp = dice[0]
    dice[0] = dice[2]
    dice[2] = dice[5]
    dice[5] = dice[3]
    dice[3] = tmp

#   1
# 3 0 2
#   4
#   5
    
# 북쪽으로
def move_up():
    tmp = dice[0]
    dice[0] = dice[4]
    dice[4] = dice[5]
    dice[5] = dice[1]
    dice[1] = tmp

# 남쪽으로
def move_down():
    tmp = dice[0]
    dice[0] = dice[1]
    dice[1] = dice[5]
    dice[5] = dice[4]
    dice[4] = tmp

for k in range(ks):
    vx, vy = queue[0]
    # print(vx, vy)
    c = cmd[k]
    
    posx = vx + dx[c-1]
    posy = vy + dy[c-1]
    
    if posx < 0 or posy < 0 or posx > n-1 or posy > m-1:
        continue
    
    queue.popleft()
    
    if c-1 == 0: # 동
        move_right()
    elif c-1 == 1: # 서
        move_left()
    elif c-1 == 2: #북
        move_up()
    elif c-1 == 3: #남
        move_down()
    
    print(dice[5])    
    queue.append((posx, posy))
    
    if maps[posx][posy] == 0:
        maps[posx][posy] = dice[0]
    else:
        dice[0] = maps[posx][posy]
        maps[posx][posy] = 0