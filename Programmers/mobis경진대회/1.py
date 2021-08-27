def solution(dice):
    check_num_li = [1, 11, 111, 1111]
    max_num = 10 ** len(dice) - 1
    for i in range(max_num):
        flag = [0] * len(dice)
        new_i = str(i)
        for check, ii in enumerate(new_i):
            ii = int(ii)
            for index, dicee in enumerate(dice):
                if ii in dicee:
                    flag[index] += 10 ** check
        check_num = check_num_li[len(new_i) - 1]
        print(check_num, new_i, flag)
        if len(dice) - flag.count(0) < len(new_i):
            summ = sum(flag)
            summ = str(summ)
            for m in summ:
                if m == '0':
                    break
            else:
                print(flag, new_i)
                return int(new_i)

solution([[1, 6, 2, 5, 3, 4], [9, 1, 1, 0, 7, 8]])

# def solution(dice):
#     answer = 0
#     flag = [0] * (10 ** len(dice) - 1)
#     binn = [0] * len(dice)
#
#
#
#     return answer

# solution([[1, 6, 2, 5, 3, 4], [9, 9, 1, 0, 7, 8]])