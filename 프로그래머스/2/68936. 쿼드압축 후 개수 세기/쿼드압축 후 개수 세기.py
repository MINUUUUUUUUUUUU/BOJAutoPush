def checking_rect(rect, cnt):
    
    total_sum = sum(sum(tmp) for tmp in rect)
    total_len = sum(len(tmp) for tmp in rect)
    
    if total_sum == 0:
        cnt[0] += 1
        return cnt
    elif total_sum == total_len:
        cnt[1] += 1
        return cnt
    else:
        half = len(rect[0]) // 2
        top_left = [row[:half] for row in rect[:half]]
        top_right = [row[half:] for row in rect[:half]]
        bottom_left = [row[:half] for row in rect[half:]]
        bottom_right = [row[half:] for row in rect[half:]]
        
        cnt = checking_rect(top_left, cnt)
        cnt = checking_rect(top_right, cnt)
        cnt = checking_rect(bottom_left, cnt)
        cnt = checking_rect(bottom_right, cnt)
        return cnt
    

def solution(arr):
    answer = []
    
    cnt = [0, 0] #0의 갯수, 1의 갯수
    answer = checking_rect(arr, cnt)
    
    return answer