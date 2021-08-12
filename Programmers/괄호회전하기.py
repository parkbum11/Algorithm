def solution(s):
    answer = 0
    if len(s) & 1: return answer
    new_s = []
    for ss in s: new_s.append(ss)
    stack = []
    while True:
        for ss in new_s:
            if ss in '{[(':
                stack.append(ss)
            else:
                if len(stack) == 0: break
                else:
        a = new_s.pop(0)
        new_s.append(a)

    return answer

solution("}]()[{")