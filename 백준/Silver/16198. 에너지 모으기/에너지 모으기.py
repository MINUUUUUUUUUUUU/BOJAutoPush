import sys

n = int(sys.stdin.readline())
marbles = list(map(int, sys.stdin.readline().split() ) )
answers = set()

def backtracking(m, energy):
    if len(m) == 2:
        return energy
        
    for i in range(1,len(m) - 1):
        # 구슬을 하나 골라서 백트래킹 진행
        tmp_m = m[:i] + m[i+1:]
        energy += m[i-1] * m[i+1]
        
        answers.add(backtracking(tmp_m, energy))
        
        energy -= m[i-1] * m[i+1] #원 상태로

backtracking(marbles, 0)
answers.discard(None)
# print(answers)
print(max(answers))
