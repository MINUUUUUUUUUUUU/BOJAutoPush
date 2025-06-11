import sys

n, game = sys.stdin.readline().split()
players = set()

for _ in range(int(n)):

    players.add(input())

# print(players)

if game == 'Y':
    answer = len(players)
elif game == 'F':
    answer = len(players) // 2
elif game == 'O':
    answer = len(players) // 3

print(answer)