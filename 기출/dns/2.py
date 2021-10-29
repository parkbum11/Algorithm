from collections import deque
def solution(v):
    answer = [0, 0]
    dr, dc = [0, 0, 1, -1], [1, -1, 0, 0]
    R, C = len(v), len(v[0])

    def bfs(i, j):
        result = 1
        q = deque()
        q.append((i, j))
        v[i][j] = 0
        while q:
            r, c = q.popleft()
            for k in range(4):
                rr, cc = r + dr[k], c + dc[k]
                if not (0 <= rr < R) or not (0 <= cc < C): continue
                if v[rr][cc] == 0: continue
                q.append((rr, cc))
                result += 1
                v[rr][cc] = 0
        return result

    for i in range(R):
        for j in range(C):
            if v[i][j] == 1:
                a = bfs(i, j)
                if a > answer[1]: answer[1] = a
                answer[0] += 1
    print(answer)
    return answer

solution([[1,1,0,1,1],[0,1,1,0,0],[0,0,0,0,0],[1,1,0,1,1],[1,0,1,1,1],[1,0,1,1,1]])