def solution(lottos, win_nums):
    cnt_zero = 0
    cnt_lott = 0
    info = [6, 6, 5, 4, 3, 2, 1]

    for i in lottos:
        if i == 0: cnt_zero += 1
        elif i in win_nums: cnt_lott += 1

    answer = [info[cnt_lott + cnt_zero], info[cnt_lott]]

    return answer

solution([44, 1, 0, 0, 31, 25], [31, 10, 45, 1, 6, 19])