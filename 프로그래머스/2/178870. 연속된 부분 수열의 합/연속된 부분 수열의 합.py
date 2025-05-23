def solution(sequence, k):
    answer = [0, 1000001]
    
    start_point = 0
    end_point = 0
    l = len(sequence)
    sum_element = sequence[0]
    
    while start_point < l and end_point < l:
        if sum_element < k:
            end_point += 1
            if end_point == l:
                break
            sum_element += sequence[end_point]
        elif sum_element > k:
            if start_point == end_point:
                end_point += 1
                if end_point == l:
                    break
                sum_element += sequence[end_point]
            sum_element -= sequence[start_point]
            start_point += 1
            if start_point == l:
                break
            
        if sum_element == k:
            if answer[1] - answer[0] > end_point - start_point:
                answer = [start_point, end_point]
            # print(start_point, end_point)
            sum_element -= sequence[start_point]
            start_point += 1
            end_point += 1
            if start_point == l:
                break
            if end_point == l:
                break
            sum_element += sequence[end_point]
    
    return answer