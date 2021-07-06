def solution(s):
    answer = ''
    info = ['zero', 'one', 'two', 'three', 'four', 'five', 'six', 'seven', 'eight', 'nine']
    info_two = '0123456789'
    s_list = []
    for i in s:
        s_list.append(i)

    cnt = 0

    string = ''
    while s_list:
        string += s_list.pop(0)
        if string in info_two:
            answer += string
            string = ''
        else:
            if string in info:
                answer += str(info.index(string))
                string = ''

    return int(answer)