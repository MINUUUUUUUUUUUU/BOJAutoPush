def solution(s):
    answer = 0
    mi = len(s)
    
    
    for i in range(1, len(s)+1):
        slice_list = []
        temp = 0
        flag = 0
        temp_count = 0
        
        while temp < len(s):
            if slice_list == []:
                slice_list.append(s[temp:temp+i])
            elif slice_list[-1] != s[temp:temp+i]:
                slice_list.append(s[temp:temp+i])
                if flag >= 1:
                    temp_count += len(str(flag+1))
                flag = 0
            elif slice_list[-1] == s[temp:temp+i]:
                flag += 1          
            temp += i        
        
        if flag >= 1:
            temp_count += len(str(flag+1))
        
        l = temp_count
        for slice_element in slice_list:
            l += len(slice_element)
            
        if l < mi:
            print(slice_list)
            mi = l
            
    answer = mi
    return answer