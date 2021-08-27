def solution(a):
    answer = []
    for aa in a:
        while True:
            if len(aa) <= 1:
                break
            elif aa[0] == 'b' and aa[-1] == 'b':
                aa = aa[1:]
                aa = aa[:-1]
            elif aa[0] == 'a':
                aa = aa[1:]
            elif aa[-1] == 'a':
                aa = aa[:-1]
        aa += '0'
        if aa[0] == 'a':
            answer.append(True)
        else:
            answer.append(False)
    print(answer)
    return answer

solution(["abab","bbaa","bababa","bbbabababbbaa"])