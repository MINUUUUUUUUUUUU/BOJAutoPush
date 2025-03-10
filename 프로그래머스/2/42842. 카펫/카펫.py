def solution(brown, yellow):
    answer = []
    
    # 전체 칸 수
    total = brown + yellow
    
    # total = width * height
    # yellow = (width - 2) * (height - 2)
    # yellow = width * height + 4 - 2 * width - 2 * height
    # yellow = total + 4 - 2 (width + height)
    # 2 (width + height) = total - yellow + 4
    # 2 (width + height) = brown + 4
    sum_width_height = int((brown + 4) / 2)
    for i in range(1,sum_width_height):
        if total == i * (sum_width_height - i):
            answer.append(sum_width_height - i)
            answer.append(i)
            break
    
    return answer