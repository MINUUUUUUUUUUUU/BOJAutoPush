def solution(n, arr1, arr2):
    answer = []
    map = [[0 for i in range(n)] for j in range(n)]
    
    for i in range(n):
        tmp = format(arr1[i],'b').zfill(n)
        tmpp = format(arr2[i],'b').zfill(n)
        
        for j in range(n):
            if tmp[j] == '1':
                map[i][j] = '#'
            elif tmpp[j] == '1':
                map[i][j] = '#'
            else:
                map[i][j] = ' '
    
    for k in map:
        answer.append(''.join(k))
    
    return answer