# dr, dc = [0, 0, -1, 1], [-1, 1, 0, 0]
# answer = -1
# def DFS(r, c, total, who, flag, board):
#     global answer
#     cnt = 0
#     for k in range(4):
#         rr, cc = r + dr[k], c + dc[k]
#         if not (0 <= rr < 4) or not (0 <= cc < 4): continue
#         if flag[rr][cc] != 0: continue
#         if board[rr][cc] == who:
#             cnt += 1
#             flag[rr][cc] = 1
#             DFS(rr, cc, total + 1, who, flag, board)
#             flag[rr][cc] = 0
#     if cnt == 0:
#         answer = max(answer, total)
#
# def solution(board):
#     global answer
#     for i in range(4):
#         for j in range(4):
#             flag = [[0] * 4 for _ in range(4)]
#             flag[i][j] = 1
#             DFS(i, j, 1, board[i][j], flag, board)
#     if answer < 2:
#         answer = -1
#     return answer
#
#
# solution([[4,2,3,2], [2,1,2,4], [1,2,3,1], [4,1,4,3]])


def solution(board):
    dr, dc = [0, 0, -1, 1], [-1, 1, 0, 0]

    answer = -1

    def DFS(r, c, total, who, flag, board):
        nonlocal answer

        cnt = 0
        for k in range(4):
            rr, cc = r + dr[k], c + dc[k]
            if not (0 <= rr < 4) or not (0 <= cc < 4): continue
            if flag[rr][cc] != 0: continue
            if board[rr][cc] == who:
                cnt += 1
                flag[rr][cc] = 1
                DFS(rr, cc, total + 1, who, flag, board)
                flag[rr][cc] = 0
        if cnt == 0:
            answer = max(answer, total)

    for i in range(4):
        for j in range(4):
            flag = [[0] * 4 for _ in range(4)]
            flag[i][j] = 1
            DFS(i, j, 1, board[i][j], flag, board)
    if answer < 2:
        answer = -1
    return answer


solution([[4,2,3,2], [2,1,2,4], [1,2,3,1], [4,1,4,3]])