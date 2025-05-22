import sys

n = int(sys.stdin.readline())
grid = [list(map(int, sys.stdin.readline().split() )) for _ in range(n)]

x, y = int(n/2), int(n/2) #grid 가운데

# N=5 인 경우, 현재 인덱스 기준으로 값이 변경되는 건
# 1칸으로 2번, 2칸으로 2번, 3칸으로 2번, 4칸으로 3번

# N=7 인 경우,
# 1칸으로 2번, 2칸으로 2번, 3칸으로 2번, 4칸으로 2번,5칸으로 2번, 6칸으로 3번

# 즉, N=N 인 경우,
# 1칸으로 2번, ... , N-2칸으로 2번, N-1칸으로 3번하면 완료되는 걸 알 수 있다.
# 그리고 총 2(n-2) + 3 = 2n - 1 번 움직이는 걸 알 수 있다.

dx = (0, 1, 0, -1)
dy = (-1, 0, 1, 0)
answer = 0

for i in range(0, 2 * n - 2):
    blocks = (i//2 + 1) #몇 칸씩 움직일 차례인지
    for j in range(blocks):
        dir_x = dx[i%4]
        dir_y = dy[i%4]
        
        x = x + dir_x
        y = y + dir_y
        
        sand = grid[x][y]
        a_sand = sand
        
        grid[x][y] = 0
        
        # 흩뿌리기
        
        # 5%
        if x + 2 * dir_x < 0 or y + 2 * dir_y < 0 or x + 2 *dir_x > n-1 or y + 2 * dir_y > n-1:
            answer += int(0.05 * sand)
        else:
            grid[x + 2 * dir_x][y + 2 * dir_y] += int(0.05 * sand)
        a_sand -= int(0.05 * sand)
        
        # 1% * 2
        tmp_x = x - dir_x + dir_y
        tmp_y = y - dir_y + dir_x
        if tmp_x < 0 or tmp_y < 0 or tmp_x > n-1 or tmp_y > n-1:
            answer += int(0.01 * sand)
        else:
            grid[tmp_x][tmp_y] += int(0.01 * sand)
        
        a_sand -= int(0.01 * sand)
        
        tmp_x = x - dir_x - dir_y
        tmp_y = y - dir_y - dir_x
        if tmp_x < 0 or tmp_y < 0 or tmp_x > n-1 or tmp_y > n-1:
            answer += int(0.01 * sand)
        else:
            grid[tmp_x][tmp_y] += int(0.01 * sand)
        a_sand -= int(0.01 * sand)
        
        # 7% * 2
        tmp_x = x + dir_y
        tmp_y = y + dir_x
        if tmp_x < 0 or tmp_y < 0 or tmp_x > n-1 or tmp_y > n-1:
            answer += int(0.07 * sand)
        else:
            grid[tmp_x][tmp_y] += int(0.07 * sand)
        a_sand -= int(0.07 * sand)
        
        tmp_x = x - dir_y
        tmp_y = y - dir_x
        if tmp_x < 0 or tmp_y < 0 or tmp_x > n-1 or tmp_y > n-1:
            answer += int(0.07 * sand)
        else:
            grid[tmp_x][tmp_y] += int(0.07 * sand)
        a_sand -= int(0.07 * sand)
        
        # 2% * 2
        tmp_x = x + 2 * dir_y
        tmp_y = y + 2 * dir_x
        if tmp_x < 0 or tmp_y < 0 or tmp_x > n-1 or tmp_y > n-1:
            answer += int(0.02 * sand)
        else:
            grid[tmp_x][tmp_y] += int(0.02 * sand)
        a_sand -= int(0.02 * sand)
        
        tmp_x = x - 2 * dir_y
        tmp_y = y - 2 * dir_x
        if tmp_x < 0 or tmp_y < 0 or tmp_x > n-1 or tmp_y > n-1:
            answer += int(0.02 * sand)
        else:
            grid[tmp_x][tmp_y] += int(0.02 * sand)
        a_sand -= int(0.02 * sand)
        
        # 10% * 2
        tmp_x = x + dir_x + dir_y
        tmp_y = y + dir_y + dir_x
        if tmp_x < 0 or tmp_y < 0 or tmp_x > n-1 or tmp_y > n-1:
            answer += int(0.1 * sand)
        else:
            grid[tmp_x][tmp_y] += int(0.1 * sand)
        a_sand -= int(0.1 * sand)
        
        tmp_x = x + dir_x - dir_y
        tmp_y = y + dir_y - dir_x
        if tmp_x < 0 or tmp_y < 0 or tmp_x > n-1 or tmp_y > n-1:
            answer += int(0.1 * sand)
        else:
            grid[tmp_x][tmp_y] += int(0.1 * sand)
        a_sand -= int(0.1 * sand)
        
        # a
        if x + dir_x < 0 or y + dir_y < 0 or x + dir_x > n-1 or y + dir_y > n-1:
            answer += a_sand
        else:
            grid[x + dir_x][y + dir_y] += a_sand
        
        
    # print(x,y, "| i:", i)

 
# 마지막 움직임
dir_x = dx[0]
dir_y = dy[0]

for _ in range(n-1):
    
    
    x = x + dir_x
    y = y + dir_y
        
    
    sand = grid[x][y]
    a_sand = sand
    
    grid[x][y] = 0
    
    # 흩뿌리기
        
    # 5%
    if x + 2 * dir_x < 0 or y + 2 * dir_y < 0 or x + 2 * dir_x > n-1 or y + 2 * dir_y > n-1:
        answer += int(0.05 * sand)
    else:
        grid[x + 2 * dir_x][y + 2 * dir_y] += int(0.05 * sand)
    a_sand -= int(0.05 * sand)
    
    # 1% * 2
    tmp_x = x - dir_x + dir_y
    tmp_y = y - dir_y + dir_x
    if tmp_x < 0 or tmp_y < 0 or tmp_x > n-1 or tmp_y > n-1:
        answer += int(0.01 * sand)
    else:
        grid[tmp_x][tmp_y] += int(0.01 * sand)
    
    a_sand -= int(0.01 * sand)
    
    tmp_x = x - dir_x - dir_y
    tmp_y = y - dir_y - dir_x
    if tmp_x < 0 or tmp_y < 0 or tmp_x > n-1 or tmp_y > n-1:
        answer += int(0.01 * sand)
    else:
        grid[tmp_x][tmp_y] += int(0.01 * sand)
    a_sand -= int(0.01 * sand)
    
    # 7% * 2
    tmp_x = x + dir_y
    tmp_y = y + dir_x
    if tmp_x < 0 or tmp_y < 0 or tmp_x > n-1 or tmp_y > n-1:
        answer += int(0.07 * sand)
    else:
        grid[tmp_x][tmp_y] += int(0.07 * sand)
    a_sand -= int(0.07 * sand)
    
    tmp_x = x - dir_y
    tmp_y = y - dir_x
    if tmp_x < 0 or tmp_y < 0 or tmp_x > n-1 or tmp_y > n-1:
        answer += int(0.07 * sand)
    else:
        grid[tmp_x][tmp_y] += int(0.07 * sand)
    a_sand -= int(0.07 * sand)
    
    # 2% * 2
    tmp_x = x + 2 * dir_y
    tmp_y = y + 2 * dir_x
    if tmp_x < 0 or tmp_y < 0 or tmp_x > n-1 or tmp_y > n-1:
        answer += int(0.02 * sand)
    else:
        grid[tmp_x][tmp_y] += int(0.02 * sand)
    a_sand -= int(0.02 * sand)
    
    tmp_x = x - 2 * dir_y
    tmp_y = y - 2 * dir_x
    if tmp_x < 0 or tmp_y < 0 or tmp_x > n-1 or tmp_y > n-1:
        answer += int(0.02 * sand)
    else:
        grid[tmp_x][tmp_y] += int(0.02 * sand)
    a_sand -= int(0.02 * sand)
    
    # 10% * 2
    tmp_x = x + dir_x + dir_y
    tmp_y = y + dir_y + dir_x
    if tmp_x < 0 or tmp_y < 0 or tmp_x > n-1 or tmp_y > n-1:
        answer += int(0.1 * sand)
    else:
        grid[tmp_x][tmp_y] += int(0.1 * sand)
    a_sand -= int(0.1 * sand)
    
    tmp_x = x + dir_x - dir_y
    tmp_y = y + dir_y - dir_x
    if tmp_x < 0 or tmp_y < 0 or tmp_x > n-1 or tmp_y > n-1:
        answer += int(0.1 * sand)
    else:
        grid[tmp_x][tmp_y] += int(0.1 * sand)
    a_sand -= int(0.1 * sand)
    
    # a
    if x + dir_x < 0 or y + dir_y < 0 or x + dir_x > n-1 or y + dir_y > n-1:
        answer += a_sand
    else:
        grid[x + dir_x][y + dir_y] += a_sand
    
# print(x,y)

print(answer)