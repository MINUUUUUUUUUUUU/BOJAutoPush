import heapq

def solution(scoville, K):
    heapq.heapify(scoville)
    
    cnt = 0
    
    while True:
        if scoville == []:
            return -1
        
        tmp = heapq.heappop(scoville)
        
        if tmp >= K:
            break
        
        if scoville == []:
            return -1
        
        cnt += 1
        tmp2 = heapq.heappop(scoville)
        v = tmp + tmp2 * 2
        heapq.heappush(scoville, v)
    
    # print(scoville)
    
    return cnt