def solution(rows, columns, queries):
    answer = []
    arr = [[0] * columns for _ in range(rows)]
    num = 1
    for i in range(rows):
        for j in range(columns):
            arr[i][j] = num
            num += 1
    for i in queries:
        r1, c1, r2, c2 = i[0] - 1, i[1] - 1, i[2] - 1, i[3] - 1,
        passed_num = arr[r1][c1]
        min_num = arr[r1][c1]
        for c in range(c1 + 1, c2 + 1):
            arr[r1][c], passed_num = passed_num, arr[r1][c]
            if passed_num < min_num: min_num = passed_num
        for r in range(r1 + 1, r2 + 1):
            arr[r][c2], passed_num = passed_num, arr[r][c2]
            if passed_num < min_num: min_num = passed_num
        for c in range(c2 - 1, c1 - 1, -1):
            arr[r2][c], passed_num = passed_num, arr[r2][c]
            if passed_num < min_num: min_num = passed_num
        for r in range(r2 - 1, r1 - 1, -1):
            arr[r][c1], passed_num = passed_num, arr[r][c1]
            if passed_num < min_num: min_num = passed_num
        answer.append(min_num)
    return answer

solution(6, 6, [[2,2,5,4],[3,3,6,6],[5,1,6,3]])