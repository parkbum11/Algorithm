import sys
sys.stdin = open('input.txt', 'r')

import copy
def Move(copyInfo, num, x, y):
    q = [[-1, -1] for _ in range(17)]
    q[num] = [-2, -2]
    for i in range(4):
        for j in range(4):
            q[copyInfo[i][j][0]] = [i, j]
    for i in range(1, 17):
        r, c = q[i][0], q[i][1]
        if r == -2 and c == -2: continue
        direc = copyInfo[r][c][1]
        for _ in range(8):
            rr, cc = r + dr[direc], c + dc[direc]
            if rr == x and cc == y:
                direc = (direc + 1) % 8
            elif rr < 0 or cc < 0 or rr >= 4 or cc >= 4:
                direc = (direc + 1) % 8
            else:
                q[copyInfo[rr][cc][0]],  q[copyInfo[r][c][0]] = q[copyInfo[r][c][0]], q[copyInfo[rr][cc][0]]
                copyInfo[r][c], copyInfo[rr][cc] = copyInfo[rr][cc], copyInfo[r][c]
                break

def Eat(info, r, c, summ):
    global answer
    copyInfo = copy.deepcopy(info)
    number = copyInfo[r][c][0]
    direction = copyInfo[r][c][1]
    copyInfo[r][c] = [-1, -1]
    Move(copyInfo, number, r, c)
    for i in copyInfo:
        print(i)
    print('--------------')
    answer = max(answer, summ + number)

    while True:
        r, c = r + dr[direction], c + dc[direction]
        if not (0 <= r < 4) or not (0 <= c < 4): break
        if copyInfo[r][c][0] == -1: continue
        Eat(copyInfo, r, c, summ + number)




# main
answer = 0
dr, dc = [-1, -1, 0, 1, 1, 1, 0, -1], [0, -1, -1, -1, 0, 1, 1, 1]
# 0 - num, 1 - dir
info = [[False] * 4 for _ in range(4)]
for i in range(4):
    a = list(map(int, input().split()))
    for j in range(4):
        info[i][j] = [a[j * 2], a[j * 2 + 1] - 1]
Eat(info, 0, 0, 0)
print(answer)