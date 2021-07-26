def solution(n,a,b):
    answer = 1
    if a & 1: a += 1
    if b & 1: b += 1
    while a != b:
        a //= 2
        b //= 2
        if a & 1: a += 1
        if b & 1: b += 1
        answer += 1
    return answer

solution(8, 4, 5)