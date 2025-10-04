def solution(numbers, hand):
    answer = ''
    
    left_pos = [1, 4]
    right_pos = [3, 4]
    
    for num in numbers:
        
        ## 왼손 고정
        if num == 1:
            answer += 'L'
            left_pos = [1, 1]
        elif num == 4:
            answer += 'L'
            left_pos = [1, 2]
        elif num == 7:
            answer += 'L'
            left_pos = [1, 3]
        ## 오른손 고정
        elif num == 3:
            answer += 'R'
            right_pos = [3, 1]
        elif num == 6:
            answer += 'R'
            right_pos = [3, 2]
        elif num == 9:
            answer += 'R'
            right_pos = [3, 3]
        ## 유동적
        elif num == 2:
            tmp1 = 2 - left_pos[0] + abs(left_pos[1] - 1) ## 왼손거리
            tmp2 = right_pos[0] - 2 + abs(right_pos[1] - 1) ## 오른손거리
            
            if tmp1 < tmp2:
                answer += 'L'
                left_pos = [2, 1]
            elif tmp1 > tmp2:
                answer += 'R'
                right_pos = [2, 1]
            elif tmp1 == tmp2:
                if hand == 'left':
                    answer += 'L'
                    left_pos = [2, 1]
                elif hand == 'right':
                    answer += 'R'
                    right_pos = [2, 1]
        elif num == 5:
            tmp1 = 2 - left_pos[0] + abs(left_pos[1] - 2) ## 왼손거리
            tmp2 = right_pos[0] - 2 + abs(right_pos[1] - 2) ## 오른손거리
            
            if tmp1 < tmp2:
                answer += 'L'
                left_pos = [2, 2]
            elif tmp1 > tmp2:
                answer += 'R'
                right_pos = [2, 2]
            elif tmp1 == tmp2:
                if hand == 'left':
                    answer += 'L'
                    left_pos = [2, 2]
                elif hand == 'right':
                    answer += 'R'
                    right_pos = [2, 2]
        elif num == 8:
            tmp1 = 2 - left_pos[0] + abs(left_pos[1] - 3) ## 왼손거리
            tmp2 = right_pos[0] - 2 + abs(right_pos[1] - 3) ## 오른손거리
            
            if tmp1 < tmp2:
                answer += 'L'
                left_pos = [2, 3]
            elif tmp1 > tmp2:
                answer += 'R'
                right_pos = [2, 3]
            elif tmp1 == tmp2:
                if hand == 'left':
                    answer += 'L'
                    left_pos = [2, 3]
                elif hand == 'right':
                    answer += 'R'
                    right_pos = [2, 3]
        elif num == 0:
            tmp1 = 2 - left_pos[0] + abs(left_pos[1] - 4) ## 왼손거리
            tmp2 = right_pos[0] - 2 + abs(right_pos[1] - 4) ## 오른손거리
            
            if tmp1 < tmp2:
                answer += 'L'
                left_pos = [2, 4]
            elif tmp1 > tmp2:
                answer += 'R'
                right_pos = [2, 4]
            elif tmp1 == tmp2:
                if hand == 'left':
                    answer += 'L'
                    left_pos = [2, 4]
                elif hand == 'right':
                    answer += 'R'
                    right_pos = [2, 4]
                    
            
    
    return answer