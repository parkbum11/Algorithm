def solution(M, load):
    answer = 0
    if max(load) > M: return -1
    load.sort(reverse=True)
    flag = [0] * len(load)
    for i in range(len(load)):
        if flag[i] == 1: continue
        flag[i] = 1
        summ = load[i]
        answer += 1
        for j in range(i, len(load)):
            if summ == M: break
            if flag[j] == 1: continue
            if summ + load[j] <= M:
                flag[j] = 1
                summ += load[j]
    # print(answer)
    return answer

solution(20, [16,15,9,17,1,3])