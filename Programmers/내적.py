
# zip 활용해봄 '음양더하기' 다른사람 답안에서 힌트얻음
def solution(a, b):
    answer = 0
    for aa, bb in zip(a, b):
        answer += (aa * bb)

    return answer