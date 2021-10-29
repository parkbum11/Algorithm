import sys
sys.stdin = open("./input.txt", "r")

from collections import deque

def Checking(r, c):
    global size, upsize
    check, check_time = 0, 0
    q = deque()
    q.append((r, c, 0))
    flag = [[0] * N for _ in range(N)]
    flag[r][c] = 1
    caneat = []
    while q:
        rr, cc, time = q.popleft()
        if time > check_time:
            if len(caneat) == 0:
                check_time += 1
            else:
                caneat.sort()
                i, j = caneat[0][0], caneat[0][1]
                position[0], position[1] = i, j
                arr[r][c], arr[i][j] = 0, 9
                check += check_time + 1
                upsize += 1
                break
        for k in range(4):
            rrr, ccc = rr + dr[k], cc + dc[k]
            if rrr < 0 or ccc < 0 or rrr >= N or ccc >= N: continue
            if flag[rrr][ccc] == 1 or arr[rrr][ccc] > size: continue
            if arr[rrr][ccc] < size and arr[rrr][ccc] != 0:
                caneat.append((rrr, ccc))
            q.append((rrr, ccc, time + 1))
            flag[rrr][ccc] = 1
    if upsize >= size:
        upsize = 0
        size += 1
    return check


N = int(input())
arr = [list(map(int, input().split())) for _ in range(N)]
size, position, upsize = 2, [], 0
dr, dc = [-1, 0, 0, 1], [0, -1, 1, 0]
answer = 0
for i in range(N):
    for j in range(N):
        if arr[i][j] == 9: position.append(i); position.append(j)

while True:
    re = Checking(position[0], position[1])
    if re == 0: break
    answer += re
print(answer)