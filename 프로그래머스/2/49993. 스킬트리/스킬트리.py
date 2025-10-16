def solution(skill, skill_trees):
    answer = 0
    
    alpha = set()
    
    for s in skill:
        alpha.add(s)
    
    for tree in skill_trees:
        # print(tree)
        
        part = ""
        for t in tree:
            if t in alpha:
                part += t
                
        # if part in skill:
            # print(part)
            # answer += 1
        
        for i in range(len(skill) + 1):
            if part == skill[:i]:
                answer += 1
                break
            
    
    return answer