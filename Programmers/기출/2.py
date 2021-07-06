def solution(inp_str):
    answer = []
    info_all = 'ABCDEFGHIJKLMNOPQRSTUVWXYZabcdefghijklmnopqrstuvwxyz0123456789~!@#$%^&*'
    info_one = 'ABCDEFGHIJKLMNOPQRSTUVWXYZ'
    info_two = 'abcdefghijklmnopqrstuvwxyz'
    info_three = '0123456789'
    info_four = '~!@#$%^&*'
    check = [0, 0, 0, 0]
    check_four_five = {}
    if len(inp_str) < 8 or len(inp_str) > 15: answer.append(1)
    for i in inp_str:
        if i not in info_all and 2 not in answer:
            answer.append(2)
        if i in info_one: check[0] = 1
        if i in info_two: check[1] = 1
        if i in info_three: check[2] = 1
        if i in info_four: check[3] = 1

        if i in check_four_five:
            check_four_five[i] += 1
            if check_four_five[i] == 4 and 4 not in answer: answer.append(4)
            if check_four_five[i] == 5 and 5 not in answer: answer.append(5)
        else:
            check_four_five[i] = 1
    if sum(check) < 3: answer.append(3)
    if len(answer) == 0: answer.append(0)
    answer.sort()
    return answer