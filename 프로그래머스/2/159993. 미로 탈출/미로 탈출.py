from collections import deque

def solution(maps):
    
    answer = 0
    n = len(maps)
    m = len(maps[0])

    board = []
    
    for i in range(n):
        tmp_list = []
        for j in range(m):
            tmp = maps[i][j]
            if tmp == 'S':
                sp = [i, j]
            elif tmp == 'E':
                ep = [i, j]
            elif tmp == 'L':
                lever = [i, j]
            
            if tmp == 'X':
                tmp_list.append(1)
            else:
                tmp_list.append(0)
        board.append(tmp_list)
    
    # print(board)
    
    direction = [ [-1, 0], [1, 0], [0, 1], [0, -1] ]
    
    queue = deque([[sp[0], sp[1], 0]]) # x, y, count
    
    visited = [[[False, 1000001] for i in range(m)] for j in range(n)]
    visited[sp[0]][sp[1]][0] = True

    lever_distance = set()
    ep_distance = set()
    
    lever_flag = 0
    ep_flag = 0
    
    while queue:
        v = queue.popleft()
        
        for d in direction:
            pos = [ v[0] + d[0] , v[1] + d[1], v[2] + 1 ]
            
            if pos[0] < 0 or pos[1] < 0 or pos[0] == n or pos[1] == m:
                continue
            
            if board[pos[0]][pos[1]] == 1:
                continue
        
            if visited[pos[0]][pos[1]][1] > pos[2]:
                if [pos[0], pos[1]] == lever and lever_flag != 2:
                    lever_distance.add(pos[2])
                    lever_flag = 1
                if [pos[0], pos[1]] == ep and lever_flag == 2:
                    ep_distance.add(pos[2])
                    ep_flag = 1
                queue.append(pos)
                visited[pos[0]][pos[1]][0] = True
                visited[pos[0]][pos[1]][1] = pos[2]
                
        if lever_flag == 1:
            lever_flag = 2
            for i in range(n):
                for j in range(m):
                    visited[i][j][1] = 1000001
            answer_lever = min(lever_distance)
            while queue:
                queue.popleft()
            queue.append([lever[0], lever[1], 0])
            
        if ep_flag:
            answer_ep = min(ep_distance)
            break
    
    if not lever_distance:
        return -1
    
    if not ep_distance:
        return -1
    
    answer = answer_lever + answer_ep
    return answer