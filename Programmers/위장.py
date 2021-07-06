# 고민 30분 다른 사람 풀이 참고함.
# 꼭 다시 풀기를 해쉬문제의 정석
def solution(clothes):
    answer = 1
    dic = {}
    for i in clothes:
        if i[1] in dic:
            dic[i[1]] += 1
        else:
            dic[i[1]] = 1
    for i in dic.values():
        answer *= (i + 1)
    return answer - 1