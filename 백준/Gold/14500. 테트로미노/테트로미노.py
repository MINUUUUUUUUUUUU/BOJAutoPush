# 브루트 포스로 구현 (추후 DFS 시도)

n, m = map(int, input().split())

paper = [list(map(int,input().split())) for i in range(n)]

cases = set()

for i in range(n):
    for j in range(m):
        
        ## 1x4, 4x1
        if i < n-3:
            cases.add(paper[i][j] + paper[i+1][j] + paper[i+2][j] + paper[i+3][j])
        if j < m-3:
            cases.add(paper[i][j] + paper[i][j+1] + paper[i][j+2] + paper[i][j+3])
        
        ## 2x2
        if i < n-1 and j < m-1:
            cases.add(paper[i][j] + paper[i+1][j] + paper[i][j+1] + paper[i+1][j+1])
            
        ## L, Z, ㅗ (6개 골라서 2개 빼기, 예외 경우 처리하기)
        ### 2x3
        if i < n-2 and j < m-1:
            temp_cases = [[0, 0], [0, 0], [0, 0]]
            temp_cases[0][0] = paper[i][j]
            temp_cases[0][1] = paper[i][j+1]
            temp_cases[1][0] = paper[i+1][j]
            temp_cases[1][1] = paper[i+1][j+1]
            temp_cases[2][0] = paper[i+2][j]
            temp_cases[2][1] = paper[i+2][j+1]
            # print(temp_cases)
            temp_sum = 0
            for temp_case in temp_cases:
                for t in temp_case:
                    temp_sum += t
            
            #  L
            cases.add(temp_sum - temp_cases[0][0] - temp_cases[1][0])
            cases.add(temp_sum - temp_cases[1][0] - temp_cases[2][0])
            cases.add(temp_sum - temp_cases[0][1] - temp_cases[1][1])
            cases.add(temp_sum - temp_cases[1][1] - temp_cases[2][1])
            
            #  Z
            cases.add(temp_sum - temp_cases[0][0] - temp_cases[2][1])
            cases.add(temp_sum - temp_cases[0][1] - temp_cases[2][0])
            
            #  ㅗ
            cases.add(temp_sum - temp_cases[0][0] - temp_cases[2][0])
            cases.add(temp_sum - temp_cases[0][1] - temp_cases[2][1])
        
        ### 3x2
        if i < n-1 and j < m-2:
            temp_cases = [[0, 0, 0], [0, 0, 0]]
            temp_cases[0][0] = paper[i][j]
            temp_cases[0][1] = paper[i][j+1]
            temp_cases[0][2] = paper[i][j+2]
            temp_cases[1][0] = paper[i+1][j]
            temp_cases[1][1] = paper[i+1][j+1]
            temp_cases[1][2] = paper[i+1][j+2]
            # print(temp_cases)
            
            temp_sum = 0
            for temp_case in temp_cases:
                for t in temp_case:
                    temp_sum += t
            
            #  L
            cases.add(temp_sum - temp_cases[0][0] - temp_cases[0][1])
            cases.add(temp_sum - temp_cases[0][1] - temp_cases[0][2])
            cases.add(temp_sum - temp_cases[1][0] - temp_cases[1][1])
            cases.add(temp_sum - temp_cases[1][1] - temp_cases[1][2])
            
            #  Z
            cases.add(temp_sum - temp_cases[0][0] - temp_cases[1][2])
            cases.add(temp_sum - temp_cases[0][2] - temp_cases[1][0])
            
            # ㅗ
            cases.add(temp_sum - temp_cases[0][0] - temp_cases[0][2])
            cases.add(temp_sum - temp_cases[1][0] - temp_cases[1][2])
        
cases_list = list(cases)
cases_list.sort()
print(cases_list[-1])