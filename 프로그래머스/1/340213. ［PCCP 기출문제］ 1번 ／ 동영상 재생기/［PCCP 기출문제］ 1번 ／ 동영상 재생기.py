def solution(video_len, pos, op_start, op_end, commands):
    answer = ''
    len_s = int(video_len[0:2]) * 60 + int(video_len[3:5])
    pos_s = int(pos[0:2]) * 60 + int(pos[3:5])
    op_start_s = int(op_start[0:2]) * 60 + int(op_start[3:5])
    op_end_s = int(op_end[0:2]) * 60 + int(op_end[3:5])
    
    for i in commands:
        
        # 건너뛰기
        if op_start_s <= pos_s <= op_end_s:
            pos_s = op_end_s
        
        # prev
        if i == 'prev':
            if pos_s <= 10:
                # 10초 이전에 오프닝이 있는 경우
                if op_start_s <= 0 <= op_end_s:
                    pos_s = op_end_s
                else:
                    pos_s = 0
            else:
                pos_s -= 10    
        
        # next
        elif i == 'next':
            if len_s < pos_s + 10:
                pos_s = len_s
            else:
                pos_s += 10            
    
    if op_start_s <= pos_s <= op_end_s:
            pos_s = op_end_s
    
    if (pos_s // 60) < 10:
        tmp1 = '0' + str(pos_s // 60)
    else:
        tmp1 = str(pos_s // 60)
        
    if (pos_s % 60) < 10:
        tmp2 = '0' + str(pos_s % 60)
    else:
        tmp2 = str(pos_s % 60)
    
    pos = tmp1 + ':' + tmp2
    answer = pos
    return answer