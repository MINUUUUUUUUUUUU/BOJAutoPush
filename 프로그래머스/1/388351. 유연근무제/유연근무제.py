def solution(schedules, timelogs, startday):
    check = [1 for i in range(len(schedules))] ## 지각 한 경우가 있으면 0으로 수정
    
    for i in range(7):
        if (startday + i) % 7 == 6 or (startday + i) % 7 == 0:
            continue
        
        for j in range(len(schedules)):
            safe_h = int(schedules[j] / 100)
            safe_m = (schedules[j] % 100) + 10
            if safe_m >= 60:
                safe_m -= 60
                safe_h += 1
            safe_time = safe_h * 100 + safe_m
            if safe_time < timelogs[j][i]:
                check[j] = 0
    
    answer = sum(check)
    return answer