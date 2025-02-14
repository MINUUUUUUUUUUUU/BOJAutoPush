def solution(array, commands):
    answer = []
    
    for command in commands:
        i, j, k = command[0], command[1], command[2]
        cutting_array = array[i-1:j]
        cutting_array.sort()
        answer.append(cutting_array[k-1])
    
    return answer