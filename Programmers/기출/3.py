from itertools import combinations
def solution(enter, leave):
    answer = [0] * len(enter)
    flag = [[0] * (max(enter) + 1) for _ in range((max(enter) + 1))]
    q_e = []
    q_l = leave[0]
    cnt = 1
    for i in enter:
        q_e.append(i)
        if len(q_e) > 1:
            li = list(combinations(q_e, 2))
            for j in li:
                flag[j[0]][j[1]] = flag[j[1]][j[0]] = 1
        while True:
            if q_l not in q_e: break
            if cnt > max(enter) - 1: break
            else:
                q_e.pop(q_e.index(q_l))
                q_l = leave[cnt]
                cnt += 1
    for i in range(1, (max(enter) + 1)):
        answer[i - 1] = sum(flag[i])
    return answer