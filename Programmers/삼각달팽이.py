def solution(n):
    answer = []
    dr, dc, dir = [1, 0, -1], [0, 1, -1], 0
    arr = []
    cnt, r, c, number = n, -1, 0, 1
    for i in range(n): arr.append([0] * (i + 1))
    while cnt:
        for i in range(cnt):
            r += dr[dir]
            c += dc[dir]
            arr[r][c] = number
            number += 1
        dir = (dir + 1) % 3
        cnt -= 1
    for i in arr: answer += i
    return answer

solution(6)