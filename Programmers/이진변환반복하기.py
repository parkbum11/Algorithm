def solution(s):
    answer = [0, 0]
    while s != '1':
        answer[1] += s.count('0')
        s = bin(len(s) - s.count('0'))[2:]
        print(s)
        answer[0] += 1
    print(answer)
    return answer
solution('01110')