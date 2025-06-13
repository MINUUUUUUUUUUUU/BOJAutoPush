from itertools import combinations

def solution(relation):
    answer = 0
    answer_cases = set()
    
    l = len(relation[0])
    nums = [i for i in range(l)]
    
    for i in range(1, l+1): # 모든 길이에 대한 시도
        
        case = list(combinations(nums, i))
        # print(case)
        
        for cas in case:
            tmp_list = []
            tmp_set = set()
            
            for r in relation:
                tmp = []
                for c in cas:
                    tmp.append(r[c])
                tmp = tuple(tmp)
                tmp_list.append(tmp)
                tmp_set.add(tmp)
            if len(tmp_list) == len(tmp_set):
                tmp_case = tuple(cas)
                flag = 1
                for j in range(1, i):
                    tmp_check = list(combinations(tmp_case, j))
                    for tc in tmp_check:
                        if tc in answer_cases:
                            flag = 0
                if flag == 1:
                    answer_cases.add(tmp_case)
                # answer += 1
        
    # print(answer_cases)
    answer = len(answer_cases)
    return answer