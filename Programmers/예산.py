def solution(d, budget):
    d.sort()
    answer = 0
    cnt = 0
    for i in d:
        if answer + i > budget:
            break
        answer += i
        cnt += 1
    return cnt




solution([1,3,2,5,4], 9)