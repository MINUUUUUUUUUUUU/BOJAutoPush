def solution(dirs):
    answer = 0
    
    visited = set()
    
    now = [0, 0]
    
    for dir in dirs:
        print(dir)
        
        if dir == 'U':
            if now[1] + 1 > 5:
                continue
            
            visited.add((tuple(now), (now[0], now[1] + 1))) # 무조건 작은게 왼쪽
            now = [now[0], now[1] + 1]
            
        elif dir == 'L':
            if now[0] - 1 < -5:
                continue
            
            visited.add(( (now[0] - 1, now[1]), tuple(now))) # 무조건 작은게 왼쪽
            now = [now[0] - 1, now[1]]
        elif dir == 'R':
            if now[0] + 1 > 5:
                continue
            
            visited.add((tuple(now), (now[0] + 1, now[1])))
            now = [now[0] + 1, now[1]]
        elif dir == 'D':
            if now[1] - 1 < -5:
                continue
            
            visited.add(((now[0], now[1] - 1), tuple(now)))
            now = [now[0], now[1] - 1]
    
    answer = len(visited)
    return answer