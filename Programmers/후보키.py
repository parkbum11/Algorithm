from itertools import combinations

def solution(relation):
    answer = 0
    info, combi = [], []
    colum, row = len(relation[0]), len(relation)
    flag = [False] * colum
    for i in range(colum):
        info.append(str(i))
    for i in range(1, colum):
        a = list(map(''.join, combinations(info, i)))
        for j in a:
            combi.append(j)
    for i in combi:
        check = set()
        for k in i:
            if flag[int(k)] == True: break
        else:
            for j in range(len(relation)):
                word = ''
                for jj in i:
                    word += relation[j][int(jj)]
                check.add(word)
        if len(check) == row:
            answer += 1
            for j in i:
                flag[int(j)] = True
    return answer

solution([
    ["100","ryan","music","2"],
    ["200","apeach","math","2"],
    ["300","tube","computer","3"],
    ["400","con","computer","4"],
    ["500","muzi","music","3"],
    ["600","apeach","music","2"]])


# 위 실패
# 성공
from itertools import combinations


def solution(relation):
    n_row = len(relation)
    n_col = len(relation[0])

    candidates = []
    for i in range(1, n_col + 1):
        candidates.extend(combinations(range(n_col), i))

    final = []
    for keys in candidates:
        tmp = [tuple([item[key] for key in keys]) for item in relation]
        if len(set(tmp)) == n_row:
            final.append(keys)

    answer = set(final[:])
    for i in range(len(final)):
        for j in range(i + 1, len(final)):
            if len(final[i]) == len(set(final[i]).intersection(set(final[j]))):
                answer.discard(final[j])

    return len(answer)