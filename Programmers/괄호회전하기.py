def solution(s):
    answer = 0
    ss = s + s
    info = {'[' : ']', '{' : '}', '(' : ')'}
    length = len(s)
    for i in range(length):
        check_s = ss[i:length + i]
        stack, couple = [], 0
        for j in check_s:
            if j in info:
                stack.append(j)
            else:
                if len(stack) == 0: break
                else:
                    a = stack.pop()
                    if info[a] != j: break
                    else:
                        if len(stack) == 0: couple += 1
        else:
            answer = couple
            break
    print(answer)
solution("[][][][]")