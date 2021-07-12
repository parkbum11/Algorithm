def solution(s):
    answer = ''
    info = ['zero', 'one', 'two', 'three', 'four', 'five', 'six', 'seven', 'eight', 'nine']
    info_two = '0123456789'
    s_list = []
    for i in s:
        s_list.append(i)
    print(info)
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


# 다른 사람 풀이

num_dic = {"zero":"0", "one":"1", "two":"2", "three":"3", "four":"4", "five":"5", "six":"6", "seven":"7", "eight":"8", "nine":"9"}

def solution(s):
    answer = s
    for key, value in num_dic.items():
        answer = answer.replace(key, value)
    return int(answer)