def solution(board):
    answer = 0
    row, col = len(board), len(board[0])

    for i in board:
        if sum(i):
            answer = 1
            break
    else:
        return 0

    for i in range(row - 1):
        for j in range(col - 1):
            if board[i + 1][j + 1]:
                board[i + 1][j + 1] = min(board[i][j], board[i + 1][j], board[i][j + 1]) + 1
                answer = max(answer, board[i + 1][j + 1])

    return answer ** 2