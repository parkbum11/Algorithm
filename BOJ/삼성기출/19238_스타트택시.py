import sys
sys.stdin = open('input.txt', 'r')

# looking for passenger
from collections import deque
def LFP(r, c):
    global R, C, P
    flag = [[0] * N for _ in range(N)]
    q = deque()
    q.append((r, c, 0))
    flag[r][c] = 1
    pp = 40001
    result = []
    while q:
        i, j, po = q.popleft()
        if po > pp or po > P: break
        if arr[i][j] != 0:
            pp = po
            result.append([i, j, arr[i][j]])
        for k in range(4):
            rr, cc = i + dr[k], j + dc[k]
            if rr < 0 or cc < 0 or rr >= N or cc >= N: continue
            if arr[rr][cc] == 1 or flag[rr][cc] == 1: continue
            flag[rr][cc] = 1
            q.append((rr, cc, po + 1))
    if len(result) == 0:
        return -1
    result.sort()
    arr[result[0][0]][result[0][1]] = 0
    R, C, P = result[0][0], result[0][1], P - pp
    return result[0][2]

# take passenger to home
def TPH(passenger):
    global R, C, P
    i, j, who = R, C, passenger - 2
    q = deque()
    q.append((i, j, 0))
    flag = [[0] * N for _ in range(N)]
    flag[i][j] = 1
    while q:
        r, c, pp = q.popleft()
        if pp > P:
            return -1
        if r == passengers[who][0] and c == passengers[who][1]:
            P += pp
            R, C = r, c
            return
        for k in range(4):
            rr, cc = r + dr[k], c + dc[k]
            if rr < 0 or cc < 0 or rr >= N or cc >= N: continue
            if arr[rr][cc] == 1 or flag[rr][cc] == 1: continue
            flag[rr][cc] = 1
            q.append((rr, cc, pp + 1))
    return -1

# main
answer = -1
dr, dc = [0, 0, 1, -1], [1, -1, 0, 0]
N, M, P = map(int, input().split())
arr = [list(map(int, input().split())) for _ in range(N)]
R, C = map(int, input().split())
R, C = R - 1, C - 1
passengers = []
for i in range(2, M + 2):
    a, b, c, d = map(int, input().split())
    arr[a - 1][b - 1] = i
    passengers.append([c - 1, d - 1])
while M != 0:
    info = LFP(R, C)
    if info == - 1:
        P = -1
        break
    ToF = TPH(info)
    if ToF == -1:
        P = -1
        break
    M -= 1
print(P)