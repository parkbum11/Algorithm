def solution(board, moves):
    answer = 0
    basket = [0]

    for i in moves:
        i -= 1
        for j in range(len(board)):
            if board[j][i] != 0:
                if basket[-1] == board[j][i]:
                    answer += 2
                    basket.pop()
                else:
                    basket.append(board[j][i])
                board[j][i] = 0
                break
    print(answer)
    return answer

solution([[0,0,0,0,0],[0,0,1,0,3],[0,2,5,0,1],[4,2,4,4,2],[3,5,1,3,1]], [1,5,3,5,1,2,1,4])