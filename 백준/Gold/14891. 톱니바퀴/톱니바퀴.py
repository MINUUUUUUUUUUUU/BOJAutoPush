import sys
from collections import deque
wheels = []
for _ in range(4):
    wheels.append(deque(map(int, sys.stdin.readline().strip())))
# print(wheels)
k = int(sys.stdin.readline())

# 12시 방향의 idx는 모두 0이다.

# 1번 톱니바퀴의 idx:2 와 2번 톱니바퀴 idx:7
# 2번 톱니바퀴의 idx:7 와 3번 톱니바퀴 idx:2
# 3번 톱니바퀴의 idx:7 와 4번 톱니바퀴 idx:2

def turning_clock(wheel):
    tmp = wheel.pop()
    wheel = deque([tmp]) + wheel
    return wheel
    
def turning_not_clock(wheel):
    tmp = wheel.popleft()
    wheel.append(tmp)
    return wheel
for _ in range(k):
    a, b = map(int, sys.stdin.readline().split()) # 톱니바퀴 번호, 방향(1 = 시계, -1 = 반시계)
    
    if b == 1:
        if a == 1:
            flag2 = 0
            flag3 = 0
            flag4 = 0
            
            if wheels[0][2] != wheels[1][6]:
                flag2 = 1
                if wheels[1][2] != wheels[2][6]:
                    flag3 = 1
                    if wheels[2][2] != wheels[3][6]:
                        flag4 = 1
                        
            wheels[0] = turning_clock(wheels[0])
            if flag2:
                wheels[1] = turning_not_clock(wheels[1])
                if flag3:
                    wheels[2] = turning_clock(wheels[2])
                    if flag4:
                        wheels[3] = turning_not_clock(wheels[3])
        elif a == 2:
            flag1 = 0
            flag3 = 0
            flag4 = 0
            
            if wheels[0][2] != wheels[1][6]:
                flag1 = 1
                
            if wheels[1][2] != wheels[2][6]:
                    flag3 = 1
                    if wheels[2][2] != wheels[3][6]:
                        flag4 = 1
            
            wheels[1] = turning_clock(wheels[1])
            if flag1:
                wheels[0] = turning_not_clock(wheels[0])
            if flag3:
                wheels[2] = turning_not_clock(wheels[2])
                if flag4:
                    wheels[3] = turning_clock(wheels[3])
        elif a == 3:
            flag1 = 0
            flag2 = 0
            flag4 = 0
            
            if wheels[2][6] != wheels[1][2]:
                flag2 = 1
                if wheels[0][2] != wheels[1][6]:
                    flag1 = 1
                    
            if wheels[2][2] != wheels[3][6]:
                flag4 = 1
            
            wheels[2] = turning_clock(wheels[2])
            if flag2:
                wheels[1] = turning_not_clock(wheels[1])
                if flag1:
                    wheels[0] = turning_clock(wheels[0])
            if flag4:
                wheels[3] = turning_not_clock(wheels[3])
                
        elif a == 4:
            flag1 = 0
            flag2 = 0
            flag3 = 0
            
            if wheels[2][2] != wheels[3][6]:
                flag3 = 1
                if wheels[2][6] != wheels[1][2]:
                    flag2 = 1
                    if wheels[0][2] != wheels[1][6]:
                        flag1 = 1
            
            wheels[3] = turning_clock(wheels[3])
            if flag3:
                wheels[2] = turning_not_clock(wheels[2])
                if flag2:
                    wheels[1] = turning_clock(wheels[1])
                    if flag1:
                        wheels[0] = turning_not_clock(wheels[0])
        
    elif b == -1:
        if a == 1:
            flag2 = 0
            flag3 = 0
            flag4 = 0
            
            if wheels[0][2] != wheels[1][6]:
                flag2 = 1
                if wheels[1][2] != wheels[2][6]:
                    flag3 = 1
                    if wheels[2][2] != wheels[3][6]:
                        flag4 = 1
            
            wheels[0] = turning_not_clock(wheels[0])
            if flag2:
                wheels[1] = turning_clock(wheels[1])
                if flag3:
                    wheels[2] = turning_not_clock(wheels[2])
                    if flag4:
                        wheels[3] = turning_clock(wheels[3])
        elif a == 2:
            flag1 = 0
            flag3 = 0
            flag4 = 0
            
            if wheels[0][2] != wheels[1][6]:
                flag1 = 1
                
            if wheels[1][2] != wheels[2][6]:
                    flag3 = 1
                    if wheels[2][2] != wheels[3][6]:
                        flag4 = 1
            
            wheels[1] = turning_not_clock(wheels[1])
            if flag1:
                wheels[0] = turning_clock(wheels[0])
            if flag3:
                wheels[2] = turning_clock(wheels[2])
                if flag4:
                    wheels[3] = turning_not_clock(wheels[3])
        elif a == 3:
            flag1 = 0
            flag2 = 0
            flag4 = 0
            
            if wheels[2][6] != wheels[1][2]:
                flag2 = 1
                if wheels[0][2] != wheels[1][6]:
                    flag1 = 1
                    
            if wheels[2][2] != wheels[3][6]:
                flag4 = 1
            
            wheels[2] = turning_not_clock(wheels[2])
            if flag2:
                wheels[1] = turning_clock(wheels[1])
                if flag1:
                    wheels[0] = turning_not_clock(wheels[0])
            if flag4:
                wheels[3] = turning_clock(wheels[3])
        elif a == 4:
            flag1 = 0
            flag2 = 0
            flag3 = 0
            
            if wheels[2][2] != wheels[3][6]:
                flag3 = 1
                if wheels[2][6] != wheels[1][2]:
                    flag2 = 1
                    if wheels[0][2] != wheels[1][6]:
                        flag1 = 1
            
            wheels[3] = turning_not_clock(wheels[3])
            if flag3:
                wheels[2] = turning_clock(wheels[2])
                if flag2:
                    wheels[1] = turning_not_clock(wheels[1])
                    if flag1:
                        wheels[0] = turning_clock(wheels[0])
            
    
    # print(wheels)

# print(wheels)

answer = 0   
for i in range(4):
    answer += wheels[i][0] * (2 ** i)
    
print(answer)