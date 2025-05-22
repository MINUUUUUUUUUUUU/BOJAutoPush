def solution(n):
    def backtracking(row):
        
        if row == n:
            return 1;
        cnt = 0
        for k in range(n):
            if check(row, k):
                board[row][k] = 1
                cnt += backtracking(row + 1)
                board[row][k] = 0
        return cnt
    
    def check(row, col):
        
        # 같은 행 체크는 필요 없음 (행마다 하나씩 queen을 두면서 작동하기 때문에)
        # 같은 열 체크
        for i in range(row):
            if board[i][col] == 1:
                return False
                
        # 대각선 체크 (-, -)
        i = row - 1
        j = col - 1
        while i >= 0 and j >= 0:
            if board[i][j] == 1:
                return False
            i -= 1
            j -= 1
        
        # 대각선 체크 (-, +)
        i = row - 1
        j = col + 1
        while i >= 0 and j < n:
            if board[i][j] == 1:
                return False
            i -= 1
            j += 1
        
        # 모든 for문에서 살아남으면 check OK    
        return True
    
    board = [[0 for _ in range(n)] for _ in range(n)]
    return backtracking(0)