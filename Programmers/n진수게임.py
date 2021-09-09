def convert(n, base):
    arr = "0123456789ABCDEF"
    q, r = divmod(n, base)
    if q == 0:
        return arr[r]
    else:
        return convert(q, base) + arr[r]


def solution(n, t, m, p):
    answer = ''
    p -= 1
    number = 0
    who = 0
    while True:
        if len(answer) >= t: break
        N_number = convert(number, n)
        for i in N_number:
            if who == p: answer += i
            who = (who + 1) % m
        number += 1
    return answer[:t]

solution(16, 16, 2, 1)