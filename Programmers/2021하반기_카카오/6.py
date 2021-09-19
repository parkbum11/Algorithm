# def solution(board, skill):
#     answer = 0
#     N = len(board)
#     M = len(board[0])
#
#     for i in skill:
#         typee, r1, c1, r2, c2, degree = i[0], i[1], i[2], i[3], i[4], i[5]
#         if typee == 1:
#             for r in range(r1, r2 + 1):
#                 for c in range(c1, c2 + 1):
#                     board[r][c] -= degree
#         else:
#             for r in range(r1, r2 + 1):
#                 for c in range(c1, c2 + 1):
#                     board[r][c] += degree
#     for i in range(N):
#         for j in range(M):
#             if board[i][j] > 0:
#                 answer += 1
#     print(answer)
#     return answer

def solution(board, skill):
    answer = 0
    N = len(board)
    M = len(board[0])
    for i in skill:
        typee, r1, c1, r2, c2, degree = i[0], i[1], i[2], i[3], i[4], i[5]

    for i in range(N):
        for j in range(M):
            building = board[i][j]
            for k in skill:
                typee, r1, c1, r2, c2, degree = k[0], k[1], k[2], k[3], k[4], k[5]
                if typee == 1: degree *= (-1)
                if r1 <= i <= r2 and c1 <= j <= c2:
                    building += degree
            if building > 0: answer += 1
    print(answer)
    return answer

solution([[5,5,5,5,5],[5,5,5,5,5],[5,5,5,5,5],[5,5,5,5,5]], [[1,0,0,3,4,4],[1,2,0,2,3,2],[2,1,0,3,1,2],[1,0,1,3,3,1]])