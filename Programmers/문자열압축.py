def solution(strings):
    answer = len(strings)
    splice_lenght = len(strings) // 2
    for i in range(1, splice_lenght + 1):
        cnt = 1
        string = ''
        new_string = ''
        for j in range(0, len(strings), i):
            if len(new_string) >= answer: break
            else:
                if string == strings[j : j + i]:
                    cnt += 1
                else:
                    if cnt > 1:
                        new_string += str(cnt)
                    new_string += string
                    string = strings[j : j + i]
                    cnt = 1
        if cnt > 1:
            new_string += str(cnt)
        new_string += string

        if len(new_string) < answer:
            answer = len(new_string)
        print(new_string)
    print(answer)
    return answer

solution("aab")

