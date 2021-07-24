def solution(dartResult):
    answer = []
    nums = '0123456789'
    num = 0
    for i, v in enumerate(dartResult):
        if v in nums:
            if type(num) == str: num += v
            else:
                answer.append(num)
                num = v
        elif v == 'S': num = int(num)
        elif v == 'D': num = int(num) ** 2
        elif v == 'T': num = int(num) ** 3
        elif v == '#': num *= -1
        elif v == '*' and len(answer): answer[-1] *= 2; num *= 2
    answer.append(num)
    return sum(answer)

solution('1D2S#10S')