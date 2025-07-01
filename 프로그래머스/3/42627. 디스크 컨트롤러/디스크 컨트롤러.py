import heapq, math

def solution(jobs):
    answer = 0
    
    start = -1
    now = 0
    
    l = len(jobs)
    queue = []
    c = 0
    
    # for _ in range(l):
    while c < l:
        for s, t in jobs:
            if start < s <= now:
                heapq.heappush(queue, [t, s])
        
        if queue:
            dist, sp = heapq.heappop(queue)
            
            start = now
            now += dist
            answer += now - sp
            c += 1
        else:
            now += 1
    
    return math.floor(answer / l)