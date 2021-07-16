def solution(n):
    answer = 0

    # 3진법
    three = ''
    while n:
        three = str(n % 3) + three
        n //= 3
    for i, v in enumerate(three):
        if v == '1': answer += (3**i) * 1
        elif v == '2': answer += (3**i) * 2
    return answer

solution(125)