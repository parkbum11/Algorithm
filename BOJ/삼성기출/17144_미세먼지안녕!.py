import sys
sys.stdin = open("./input.txt", "r")

def diffusion():
    dr, dc = [0, 0, 1, -1], [1, -1, 0, 0]
    li = []
    for r in range(R):
        for c in range(C):
            if arr[r][c] > 0: li.append((r, c))
    cal = []
    for r, c in li:
        canDiff = 0
        sizeDiff = arr[r][c] // 5
        if arr[r][c] < 5: continue
        for k in range(4):
            rr, cc = r + dr[k], c + dc[k]
            if rr < 0 or cc < 0 or rr >= R or cc >= C: continue
            if arr[rr][cc] == -1: continue
            canDiff += 1
            cal.append((rr, cc, sizeDiff))
        cal.append((r, c, -(sizeDiff * canDiff)))
    for r, c, num in cal:
        arr[r][c] += num

def cleanUp(u, d):
    # 위
    dir_r, dir_c = [0, -1, 0, 1], [1, 0, -1, 0]
    dump = 0
    r, c, dir = u, 0, 0
    while True:
        r, c = r + dir_r[dir], c + dir_c[dir]
        if r == u and c == 0: break
        if r < 0 or c < 0 or r >= R or c >= C:
            r, c = r - dir_r[dir], c - dir_c[dir]
            dir = (dir + 1) % 4
            continue
        arr[r][c], dump = dump, arr[r][c]
    # 아래
    dir_r[1] = 1
    dir_r[3] = -1
    dump = 0
    r, c, dir = d, 0, 0
    while True:
        r, c = r + dir_r[dir], c + dir_c[dir]
        if r == d and c == 0: break
        if r < 0 or c < 0 or r >= R or c >= C:
            r, c = r - dir_r[dir], c - dir_c[dir]
            dir = (dir + 1) % 4
            continue
        arr[r][c], dump = dump, arr[r][c]

R, C, T = map(int, input().split())
arr = [list(map(int, input().split())) for _ in range(R)]

up, down = 0, 0
answer = 0

# 청소기 위치 찾기
for r in range(R):
    if arr[r][0] == -1:
        up = r
        down = r + 1
        break
while answer != T:
    answer += 1
    # 확산
    diffusion()
    # 청소
    cleanUp(up, down)
# 남은 미세먼지 cal
result = 2
for a in arr: result += sum(a)
print(result)
