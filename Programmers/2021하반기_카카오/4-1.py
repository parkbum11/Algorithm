from itertools import combinations
import copy
def solution(n, info):
    answer = []
    answer_score = -55
    info = info[::-1]
    li = []
    apach_got = []

    for i in range(11):
        if info[i] > 0: apach_got.append(i)
        # (필요 화살, 점수)
        li.append((info[i] + 1, i))

    apach_score = sum(apach_got)

    for i in range(1, 12):
        combi = list(combinations(li, i))
        print(combi)

        for j in combi:
            lion_score = 0
            apa_score = apach_score
            summ = 0

            for num_n, score in j:
                summ += num_n

                if score in apach_got:
                    apa_score -= score

                lion_score += score

            if summ <= n and apa_score < lion_score:
                li_j = list(j)

                for _ in range(n - summ):
                    li_j.append((1, 0))

                if answer_score == lion_score:
                    answer.append(copy.deepcopy(li_j))

                elif answer_score < lion_score:
                    answer_score = lion_score
                    answer = [copy.deepcopy(li_j)]

    if len(answer) == 0: return [-1]

    new_answer = []

    for i in answer:
        a = [0] * 11
        for num_n, score in i:
            a[score] += num_n
        new_answer.append(a)
    new_answer.sort()
    return new_answer[-1][::-1]


solution(10, [0,0,0,0,0,0,0,0,3,4,3])