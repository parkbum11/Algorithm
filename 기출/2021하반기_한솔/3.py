def solution(s):
    answer = len(s)
    length = len(s)

    divisor = []
    for i in range(1, length):
        if length % i == 0:
            divisor.append(i)
    print(divisor)
    for num in divisor:
        ss = ''
        for i in range(0, length, num):
            if not ss:
                ss = s[i:i + num]
                continue
            if ss != s[i:i + num]:
                break
        else:
            answer = num
            break
    print(answer)
    return answer

solution("a")