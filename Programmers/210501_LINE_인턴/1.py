def solution(inputString):
    answer = 0
    stack = []
    for i, v in enumerate(inputString):
        if v not in ['(', ')', '{', '}', '[', ']', '<', '>']:
            continue
        elif v == '(' or v == '{' or v == '[' or v == '<':
            stack.append(v)
        else:
            if len(stack) == 0:
                return (-1) * i
            else:
                if v == ')' and stack[-1] == '(':
                    stack.pop(-1)
                    answer += 1
                elif v == '}' and stack[-1] == '{':
                    stack.pop(-1)
                    answer += 1
                elif v == ']' and stack[-1] == '[':
                    stack.pop(-1)
                    answer += 1
                elif v == '>' and stack[-1] == '<':
                    stack.pop(-1)
                    answer += 1
                else:
                    return (-1) * i
    if len(stack) != 0:
        return (-1) * (len(inputString) - 1)
    return answer