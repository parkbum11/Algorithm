def solution(progresses, speeds):
    answer = []
    info = []

    for i in range(len(progresses)):
        num = (100 - progresses[i]) // speeds[i]
        if (100 - progresses[i]) % speeds[i] != 0:
            num += 1
        info.append(num)

    day = info[0]
    cnt = 1
    for i in info[1:]:
        if day >= i:
            cnt += 1
        else:
            answer.append(cnt)
            day = i
            cnt = 1
    answer.append(cnt)
    return answer