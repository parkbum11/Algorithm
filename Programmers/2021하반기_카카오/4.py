answer = {}
answer_score = 0

def shot(n, lion_info, info, index):
    global answer, answer_score
    if n == 0:
        score = 0
        for i in range(11):
            if info[i] == 0 and lion_info[i] == 0: continue
            if info[i] >= lion_info[i]:
                score -= i
            else:
                score += i
        if score <= 0: return
        if answer_score <= score:
            str_lion_info = ''
            for i in lion_info:
                str_lion_info += str(i)
            if score not in answer:
                answer[score] = set()
            answer[score].add(str_lion_info)
        return
    for i in range(index, 11):
        if info[i] < lion_info[i]:
            shot(n, lion_info, info, index + 1)
        else:
            lion_info[i] += 1
            shot(n - 1, lion_info, info, index)
            lion_info[i] -= 1

def solution(n, info):
    info = info[::-1]
    shot(n, [0] * 11, info, 0)

    if len(answer) == 0:
        return [-1]
    li = max(sorted(answer.keys()))
    max_li = []
    for i in answer[li]:
        max_li.append(i)
    max_li.sort()
    real_answer = []
    for i in max_li[-1][::-1]:
        real_answer.append(int(i))
    return answer


solution(5, [2,1,1,1,0,0,0,0,0,0,0])