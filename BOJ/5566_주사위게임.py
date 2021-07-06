import sys
sys.stdin = open('input.txt','r')

game = [0]
location = 1
N, M = map(int, input().split())
for _ in range(N):
    num = int(input())
    game.append(num)

for m in range(1, M + 1):
    num = int(input())
    location = location + num
    if location >= N:
        print(m)
        break
    location += game[location]
    if location >= N:
        print(m)
        break
