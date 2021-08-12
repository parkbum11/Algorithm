from collections import deque
def solution(N, road, K):
    answer = 0
    arr = [[0] * (N + 1) for _ in range(N + 1)]
    flag = [987654321] * (N + 1)
    flag[1] = 0
    for i in road:
        if arr[i[0]][i[1]] != 0 and arr[i[0]][i[1]] < i[2]: continue
        arr[i[0]][i[1]] = arr[i[1]][i[0]] = i[2]
    print(arr)
    q = deque()
    for i in range(1, N + 1):
        if arr[1][i] != 0 and arr[1][i] <= K:
            q.append((i, arr[1][i]))
            flag[i] = arr[1][i]
    while q:
        where, howlong = q.popleft()
        if howlong > K: continue
        for j in range(1, N + 1):
            if arr[where][j] != 0 and flag[j] >= (arr[where][j] + howlong):
                q.append((j, arr[where][j] + howlong))
                flag[j] = (arr[where][j] + howlong)
    for f in flag:
        if f <= K: answer += 1
    return answer

# solution(5, [[1,2,1],[2,3,3],[5,2,2],[1,4,2],[5,3,1],[5,4,2]], 3)
solution(6, [[1,2,1],[1,3,2],[2,3,2],[3,4,3],[3,5,2],[3,5,3],[5,6,1]], 4)