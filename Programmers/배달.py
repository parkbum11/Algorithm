from collections import deque
def solution(N, road, K):
    arr = [[0] * (N + 1) for _ in range(N + 1)]
    flag = [0] * (N + 1)
    flag[1] = 1
    for i in road:
        arr[i[0]][i[1]] = arr[i[1]][i[0]] = i[2]
    q = deque()
    for i in range(1, N + 1):
        if arr[1][i] != 0 and arr[1][i] <= K:
            q.append((i, arr[1][i]))
            flag[i] = 1
    while q:
        where, howlong = q.popleft()
        for j in range(1, N + 1):
            if arr[where][j] != 0 and (arr[where][j] + howlong) <= K and flag[j] == 0:
                q.append((j, arr[where][j] + howlong))
    print(sum(flag) + 1)
    return sum(flag) + 1

solution(6, [[1,2,1],[1,3,2],[2,3,2],[3,4,3],[3,5,2],[3,5,3],[5,6,1]], 4)