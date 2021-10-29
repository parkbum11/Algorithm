import sys
sys.stdin = open("../input.txt", "r")

from collections import deque

def BFS(r, c):
    q = deque()
    q.append((r, c))
    arr[r][c] = 0
    flag = []
    cnt = 0
    people = 0
    while q:
        rr, cc = q.popleft()
        cnt += 1
        people += li[rr][cc]
        flag.append((rr, cc))
        for k in range(4):
            rrr, ccc = rr + dr[k], cc + dc[k]
            if rrr < 0 or rrr >= N or ccc < 0 or ccc >= N: continue
            if arr[rrr][ccc] == 0: continue
            arr[rrr][ccc] = 0
            q.append((rrr, ccc))
    new_people = people // cnt
    for i, j in flag:
        li[i][j] = new_people

def checking():
    check = 0
    arr = [[0] * N for _ in range(N)]
    for i in range(N):
        for j in range(N):
            for k in range(4):
                rr, cc = i + dr[k], j + dc[k]
                if rr < 0 or rr >= N or cc < 0 or cc >= N: continue
                if arr[rr][cc] == 1: continue
                if L <= abs(li[i][j] - li[rr][cc]) <= R:
                    check += 1
                    arr[rr][cc] = 1
    if check == 0: return 0
    return arr

answer = 0
dr, dc = [0, 0, -1, 1], [-1, 1, 0, 0]
N, L, R = map(int, input().split())
li = [list(map(int, input().split())) for _ in range(N)]

while True:
    arr = checking()
    if arr == 0: break
    answer += 1
    for i in range(N):
        for j in range(N):
            if arr[i][j] == 1:
                BFS(i, j)
print(answer)

