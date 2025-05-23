from collections import deque

def solution(queue1, queue2):
    
    queue1 = deque(queue1)
    queue2 = deque(queue2)
    
    queue1_sum = sum(queue1) # 어차피
    queue2_sum = sum(queue2) # 자주쓸거다
    total_sum = queue1_sum + queue2_sum
    
    if total_sum % 2 == 1: # 최종 합이 홀수면 어떤 짓을 해도 안된다
        return -1
    
    expected = int(total_sum / 2) # 각 queue 마다 되어야하는 합의 값
    
    l = 2 * len(queue1) + 2 * len(queue2)
    count = 0
    
    for _ in range(l):
        # print(queue1, queue2)
        if queue1_sum == expected:
            return count
        if queue1_sum < expected:
            val = queue2.popleft()
            queue1.append(val)
            queue1_sum += val
            queue2_sum -= val
        else:
            val = queue1.popleft()
            queue2.append(val)
            queue1_sum -= val
            queue2_sum += val
        count += 1
    
    return -1