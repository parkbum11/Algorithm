import sys
sys.stdin = open('input.txt', 'r')

# 시간초과
from collections import deque
def texi_pass_BFS(st_r, st_c, now_power):
    global result, te_r, te_c
    q = deque()
    q.append((st_r, st_c, now_power))
    flag = [[0] * N for _ in range(N)]
    pass_li = []
    max_po = N * 2
    while q:
        r, c, po = q.popleft()
        flag[r][c] = 1
        if po > max_po or po > result: continue
        if type(arr[r][c]) != str:
            if arr[r][c] > 1 and (r, c) not in pass_li:
                max_po = po
                pass_li.append((r, c))
        for i in range(4):
            rr, cc = r + dr[i], c + dc[i]
            if rr < 0 or rr >= N or cc < 0 or cc >= N: continue
            if flag[rr][cc] == 1 or arr[rr][cc] == 1: continue
            q.append((rr, cc, po + 1))
    if len(pass_li) == 0:
        result = -1
        return

    pass_li.sort()
    end = str(arr[pass_li[0][0]][pass_li[0][1]])
    arr[pass_li[0][0]][pass_li[0][1]] = 0
    q.append((pass_li[0][0], pass_li[0][1], 0))
    flag = [[0] * N for _ in range(N)]
    a = 0
    while q:
        r, c, po = q.popleft()
        flag[r][c] = 1
        if result - max_po - po < 0:
            result = -1
            break
        if arr[r][c] == end:
            result = result - max_po + po
            te_r, te_c = r, c
            a = 1
            break
        for i in range(4):
            rr, cc = r + dr[i], c + dc[i]
            if rr < 0 or rr >= N or cc < 0 or cc >= N: continue
            if flag[rr][cc] == 1 or arr[rr][cc] == 1: continue
            q.append((rr, cc, po + 1))
    if a == 0: result = -1

# main
dr, dc = [0, 0, -1, 1], [-1, 1, 0, 0]
N, M, power = map(int, input().split())
arr = [list(map(int, input().split())) for _ in range(N)]
texi_r, texi_c = map(int, input().split())

for i in range(2, M + 2):
    st_r, st_c, en_r, en_c = map(int, input().split())
    arr[st_r - 1][st_c - 1], arr[en_r - 1][en_c - 1] = i, str(i)

te_r, te_c, result = texi_r - 1, texi_c - 1, power

for i in range(M):
    texi_pass_BFS(te_r, te_c, 0)
    if result == -1: break

print(result)