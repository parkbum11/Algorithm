import sys
sys.stdin = open('input.txt', 'r')

from collections import deque

def rotate():
    ret = [[0] * N for _ in range(N)]
    for r in range(N):
        for c in range(N):
            ret[N - 1 - c][r] = arr[r][c]
    for i in range(N):
        for j in range(N):
            arr[i][j] = ret[i][j]

def Move():
    for j in range(N):
        for i in range(N - 1, -1, -1):
            if arr[i][j] < 0: continue
            index = i + 1
            canMove = None
            while index != N:
                if arr[index][j] == -1: break
                if arr[index][j] == -2:
                    canMove = [index, j]
                index += 1
            if canMove:
                arr[canMove[0]][canMove[1]], arr[i][j] = arr[i][j], arr[canMove[0]][canMove[1]]

def LFG(i, j, color):
    global flag, info
    standard_block = None
    rainbow_num = 0
    all_num = 1
    blocks = [(i, j)]

    li = [[0] * N for _ in range(N)]
    li[i][j] = 1
    q = deque()
    q.append((i, j))
    while q:
        r, c = q.popleft()
        for k in range(4):
            rr, cc = r + dr[k], c + dc[k]
            if not (0 <= rr < N) or not (0 <= cc < N): continue
            if li[rr][cc] == 1: continue
            if arr[rr][cc] == 0 or arr[rr][cc] == color:
                if arr[rr][cc] == 0:
                    rainbow_num += 1
                elif arr[rr][cc] == color:
                    flag[rr][cc] = 1
                all_num += 1
                blocks.append((rr, cc))
                q.append((rr, cc))
                li[rr][cc] = 1
    blocks.sort()
    for block in blocks:
        if arr[block[0]][block[1]] != 0:
            standard_block = block
            break
    result = [all_num, rainbow_num, standard_block[0], standard_block[1], blocks]
    for i in range(4):
        if result[i] == info[i]: continue
        elif result[i] > info[i]:
            info = result
            break
        else:
            break

# main
answer = 0
N, M = map(int, input().split())
arr = [list(map(int, input().split())) for _ in range(N)]
dr, dc = [0, 0, 1, -1], [1, -1, 0, 0]

while True:
    flag = [[0] * N for _ in range(N)]
    info = [0, 0, -1, -1, None]
    # step 1
    for i in range(N):
        for j in range(N):
            if flag[i][j] == 0 and arr[i][j] >= 1:
                flag[i][j] = 1
                LFG(i, j, arr[i][j])
    # step 2
    if info[0] < 2: break
    answer += info[0] ** 2
    for i, j in info[4]: arr[i][j] = -2
    # step 3
    Move()
    # step 4
    rotate()
    # step 5
    Move()
print(answer)