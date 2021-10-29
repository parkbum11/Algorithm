import sys
sys.stdin = open('input.txt', 'r')

def Seat(who, fri):
    candi, max_score = [], -1
    for i in range(N):
        for j in range(N):
            score = 0
            if arr[i][j] != 0: continue
            for k in range(4):
                r, c = i + dr[k], j + dc[k]
                if not (0 <= r < N) or not (0 <= c < N): continue
                if arr[r][c] == 0: score += 1
                elif arr[r][c] in fri: score += 10
            if score > max_score:
                max_score = score
                candi = [(i, j)]
            elif score == max_score:
                candi.append((i, j))
    candi.sort()
    arr[candi[0][0]][candi[0][1]] = who

# main
answer = 0
dr, dc = [-1, 0, 0, 1], [0, -1, 1, 0]
N = int(input())
arr = [[0] * N for _ in range(N)]
info = [[None] for _ in range(N ** 2 + 1)]
for _ in range(N ** 2):
    li = list(map(int, input().split()))
    who, friends = li[0], li[1:]
    info[who] = friends
    Seat(who, friends)
for i in range(N):
    for j in range(N):
        n = 0
        for k in range(4):
            r, c = i + dr[k], j + dc[k]
            if not (0 <= r < N) or not (0 <= c < N): continue
            if arr[r][c] in info[arr[i][j]]: n += 1
        answer += (10 ** n) // 10
print(answer)
