import sys
sys.stdin = open('input.txt', 'r')

from collections import deque
def BigSizeIce(i, j):
    q = deque()
    q.append((i, j))
    arr[i][j] = 0
    cnt = 1
    while q:
        r, c = q.popleft()
        for k in range(4):
            rr, cc = r + dr[k], c + dc[k]
            if not (0 <= rr < 2 ** N) or not (0 <= cc < 2 ** N): continue
            if arr[rr][cc] == 0: continue
            q.append((rr, cc))
            arr[rr][cc] = 0
            cnt += 1
    return cnt

def ControlIce():
    m = [[4] * (2 ** N) for _ in range(2 ** N)]
    for r in range(2 ** N):
        for c in range(2 ** N):
            if r <= 0 or r >= 2 ** N - 1: m[r][c] -= 1
            if c <= 0 or c >= 2 ** N - 1: m[r][c] -= 1
            if arr[r][c] > 0: continue
            cnt = 0
            for k in range(4):
                rr, cc = r + dr[k], c + dc[k]
                if not (0 <= rr < 2 ** N) or not (0 <= cc < 2 ** N):
                    continue
                m[rr][cc] -= 1
    for r in range(2 ** N):
        for c in range(2 ** N):
            if m[r][c] < 3:
                arr[r][c] -= 1
                if arr[r][c] < 0: arr[r][c] = 0

def Rotate90(i, j, length):
    m = [[0] * length for _ in range(length)]
    for r in range(length):
        for c in range(length):
            m[c][length - 1 - r] = arr[r + i][c + j]
    for r in range(length):
        for c in range(length):
            arr[r + i][c + j] = m[r][c]

answer = [0, 0]
dr, dc = [0, 0, 1, -1], [1, -1, 0, 0]
N, Q = map(int, input().split())
arr = [list(map(int, input().split())) for _ in range(2 ** N)]
L_list = list(map(int, input().split()))
for l in L_list:
    for i in range(0, 2 ** N, 2 ** l):
        for j in range(0, 2 ** N, 2 ** l):
            Rotate90(i, j, 2 ** l)
    ControlIce()
for r in arr:
    answer[0] += sum(r)
for i in range(2 ** N):
    for j in range(2 ** N):
        if arr[i][j] != 0:
            size = BigSizeIce(i, j)
            answer[1] = max(answer[1], size)
print(answer[0])
print(answer[1])