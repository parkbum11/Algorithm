# 내가 한거 아님

import re
def solution(expression):
    answer = []
    combinations = [['+','-','*'],['+','*','-'],['-','+','*'],['-','*','+'],['*','-','+'],['*','+','-']]
    for combination in combinations:
        operand = re.split('[*+-]',expression)
        operator = re.split('[0-9]+',expression)[1:-1]
        print(operand, operator)
        for comb in combination:
            while comb in operator:
                idx = operator.index(comb)
                operand[idx] = str(eval(operand[idx] + comb + operand[idx+1]))
                del operand[idx+1]
                del operator[idx]
        answer.append(abs(int(operand[0])))
    return max(answer)

solution("100-200*300-500+20")