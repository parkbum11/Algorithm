import sys
sys.stdin = open('input.txt', 'r')

def NewCloud():
    global cloud
    new_one = []
    cloud_arr = [[0] * N for _ in range(N)]
    for i in cloud:
        cloud_arr[i[0]][i[1]] = 1
    for i in range(N):
        for j in range(N):
            if arr[i][j] >= 2 and cloud_arr[i][j] == 0:
                new_one.append([i, j])
                arr[i][j] -= 2
    cloud = new_one

def CloneWater():
    global cloud
    for i, j in cloud:
        arr[i][j] += 1
    for i in cloud:
        r, c = i[0], i[1]
        cnt = 0
        for k in range(1, 8, 2):
            rr, cc = r + dr[k], c + dc[k]
            if not (0 <= rr < N) or not ( 0 <= cc < N): continue
            if arr[rr][cc] > 0: cnt += 1
        arr[r][c] += cnt

def Move(d, n):
    global cloud
    n %= N
    for i in range(len(cloud)):
        r, c = ((cloud[i][0] + (dr[d] * n)) + N) % N, ((cloud[i][1] + (dc[d] * n)) + N) % N
        cloud[i] = [r, c]

answer = 0
dr, dc = [0, -1, -1, -1, 0, 1, 1, 1], [-1, -1, 0, 1, 1, 1, 0, -1]
N, M = map(int, input().split())
arr = [list(map(int, input().split())) for _ in range(N)]
cloud = [[N - 1, 0], [N - 1, 1], [N - 2, 0], [N - 2, 1]]
for i in range(M):
    direc, cnt = map(int, input().split())
    direc -= 1
    Move(direc, cnt)
    CloneWater()
    NewCloud()
for i in arr:
    answer += sum(i)
print(answer)