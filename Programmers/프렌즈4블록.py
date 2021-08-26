def solution(m, n, board):
    # m - r, n - l
    answer = 0
    new_board = [[0] * n for _ in range(m)]
    dr, dc = [0, 1, 0, 1], [0, 0, 1, 1]
    for i, b in enumerate(board):
        for j, bb in enumerate(b):
            new_board[i][j] = bb
    while True:
        li = []
        for i in range(m - 1):
            for j in range(n - 1):
                if new_board[i][j] == 0: continue
                for k in range(1, 4):
                    if new_board[i][j] != new_board[i + dr[k]][j + dc[k]]: break
                else: li.append((i, j))
        for i, j in li:
            for k in range(4):
                new_board[i + dr[k]][j + dc[k]] = 0
        if len(li) == 0: break
        # 내리기
        for j in range(n):
            for i in range(m - 1, 0, -1):
                if new_board[i][j] != 0: continue
                i_index = i - 1
                while i_index >= 0:
                    if new_board[i_index][j] != 0:
                        new_board[i][j] = new_board[i_index][j]
                        new_board[i_index][j] = 0
                        break
                    i_index -= 1
    for i in new_board:
        for j in i:
            if j == 0: answer += 1
    return answer

solution(6, 6, ["TTTANT", "RRFACC", "RRRFCC", "TRRRAA", "TTMMMF", "TMMTTJ"])