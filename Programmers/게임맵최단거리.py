from collections import deque

def BFS(n, m, maps):
    result = -1
    dr, dc = [0, 0, -1, 1], [-1, 1, 0, 0]
    flag = [[False] * m for _ in range(n)]
    q = deque()
    q.append((0, 0, 1))
    flag[0][0] = True
    while q:
        r, c, cnt = q.popleft()
        if r == n - 1 and c == m - 1: return cnt
        for i in range(4):
            rr, cc = r + dr[i], c + dc[i]
            if rr < 0 or rr >= n or cc < 0 or cc >= m or maps[rr][cc] == 0 or flag[rr][cc] == True: continue
            q.append((rr, cc, cnt + 1))
            flag[rr][cc] = True
    return result

def solution(maps):
    answer = BFS(len(maps), len(maps[0]), maps)
    print(answer)
    return answer

solution([[1,0,1,1,1],[1,0,1,0,1],[1,0,1,1,1],[1,1,1,0,1],[0,0,0,0,1]])