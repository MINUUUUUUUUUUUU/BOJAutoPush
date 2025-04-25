from collections import deque

n, m = map(int, input().split())
specials = [list(map(int,input().split())) for i in range(n+m)]
start_point = []
end_point = []

for a,b in specials:
    start_point.append(a-1)
    end_point.append(b-1)




visited = [False for i in range(100)]
# print(visited)
    
queue = deque([[0, 0]]) ## 0번째 칸에서 시작, 0번째 이동
visited[0] = True

while queue:
    v = queue.popleft()
    # print(v[0], end = ' ')
    
    for i in [1,2,3,4,5,6]:
        temp_location = v[0] + i
        
        for j in range(len(start_point)):
            if start_point[j] == temp_location:
                temp_location = end_point[j]
        
        if temp_location >= 100:
            continue
        elif temp_location == 99:
            print(v[1] + 1)
            exit()
        
        if temp_location < 100 and not visited[temp_location]:
            queue.append([temp_location, v[1] + 1])
            visited[temp_location] = True
    
    