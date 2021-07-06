# first answer by me (효율성 불통)
def solution(participant, completion):
    answer = ''
    flag = [0] * len(completion)
    for i in participant:
        for j in range(len(completion)):
            if flag[j] == 1:
                continue
            else:
                if completion[j] == i:
                    flag[j] = 1
                    break
        else:
            return i
    return answer

# secon answer 효율성까지 통과
def solution(participant, completion):
    answer = ''
    participant.sort()
    completion.sort()

    for i in range(len(completion)):
        if participant[i] != completion[i]:
            answer = participant[i]
            break
    else:
        return participant[-1]
    return answer

# 다른 사람 풀이
import collections


def solution(participant, completion):
    answer = collections.Counter(participant) - collections.Counter(completion)
    print(answer)
    return list(answer.keys())[0]
