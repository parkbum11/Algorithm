# you can write to stdout for debugging purposes, e.g.
# print("this is a debug message")


def solution(S):
    delete_li = ['AB', 'BA', 'CD', 'DC']
    stack = []
    answer = ''
    for str in S:
        if len(stack) == 0:
            stack.append(str)
        else:
            if (str + stack[-1]) in delete_li:
                stack.pop(-1)
            else:
                stack.append(str)
    for i in stack:
        answer += i
    print(answer)
    return answer

solution('CABABD')
