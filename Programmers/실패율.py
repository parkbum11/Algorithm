def solution(N, stages):
    answer = []
    info = {}
    people = len(stages)
    for i in range(1, N + 1):
        if people == 0:
            if people in info:
                info[people].append(i)
            else:
                info[people] = [i]
        else:
            if stages.count(i) / people in info:
                info[stages.count(i) / people].append(i)
            else:
                info[stages.count(i) / people] = [i]
            people -= stages.count(i)
    res = sorted(info.items(), reverse=True)
    # print(res)
    for i in res:
        for j in i[1]:
            answer.append(j)
    return answer

solution(8, [2, 1, 2, 6, 2, 4, 3, 3])