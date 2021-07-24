def solution(numbers):
    answer = []
    flag = [False] * ((max(numbers) + 1) * 2)
    for i in range(len(numbers) - 1):
        for j in range(i + 1, len(numbers)):
            summ = numbers[i] + numbers[j]
            if flag[summ] == False: flag[summ] = True; answer.append(summ)
    answer.sort()
    return answer