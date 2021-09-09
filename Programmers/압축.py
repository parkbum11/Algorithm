def solution(msg):
    answer = []
    dict = {}
    for i in range(1, 27):
        dict[chr(i + 64)] = i
    index = 0
    plus = 1
    dict_num = 27
    while True:
        if index + plus > len(msg):
            if len(msg) - 1 >= index:
                answer.append(dict[msg[index:]])
            break
        if msg[index: index + plus] not in dict:
            dict[msg[index: index + plus]] = dict_num
            answer.append(dict[msg[index: index + plus - 1]])
            dict_num += 1
            index += (plus - 1)
            plus = 1
        else:
            plus += 1
    return answer

solution('TOBEORNOTTOBEORTOBEORNOT')